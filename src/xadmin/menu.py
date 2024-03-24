from django.urls import resolve
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.encoding import smart_str
from src.xadmin.utils import load_from_json


class MenuList(object):

    def __init__(self, request, mod_name, site):
        self.request = request
        self.site = site
        self.mod_name = mod_name
        self.default_access = None
        self.standard_modules = settings.STANDARD_MODULES if not settings.ENABLE_WDMS else settings.WDMS_MODULES
        self.system_menus = {}
        self.user = request.user
        enable_accounts = True
        enable_core = True
        enable_contact = True
        enable_application = True
        enable_blogs = True
        if not self.user.is_patient:
            modules = self.user.get_preferences('modules', None)
            if modules:
                enable_accounts = modules.get('accounts', 0)
                enable_core = modules.get('core', 0)
                enable_contact = modules.get('contact', 0)
                enable_application = modules.get('application', 0)
                enable_blogs = modules.get('blogs', 0)
        if enable_accounts and self.user.has_perm('accounts.enter_accounts_module'):
            from src.accounts import APP_NAME, get_menu
            self.accounts_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(
                self.accounts_menu, APP_NAME)

    def filter_eligible_menu(self, menu_group, app_label):
        user = self.request.user
        menu_groups = menu_group.get('menu_groups', [])
        for (index, group) in enumerate(menu_groups):
            m_items = group.get('menus', [])
            if not m_items:
                continue
            _len = len(m_items)
            for (i, item) in enumerate(reversed(m_items), start=1):
                model_name = item.get('model_name', '').lower()
                if len(model_name) > 0:
                    info = model_name.split('.')
                    if len(info) == 1:
                        _app_label = app_label
                        _model_name = info[0]
                    elif len(info) == 2:
                        (_app_label, _model_name) = info
                        if not user.has_model_op_perms(_app_label, _model_name):
                            m_items.pop(_len - i)
                        url = item.get('url', '')
                        url_name = resolve(url).url_name
                        view_perm_name = '{app}.view_{url_name}'.format(
                            app=app_label, url_name=url_name)
                        if not user.has_perm(view_perm_name):
                            m_items.pop(_len - i)
                    if not user.has_model_op_perms(_app_label, _model_name):
                        m_items.pop(_len - i)
                else:
                    url = item.get('url', '')
                    url_name = resolve(url).url_name
                    view_perm_name = '{app}.view_{url_name}'.format(
                        app=app_label, url_name=url_name)
                    if not user.has_perm(view_perm_name):
                        m_items.pop(_len - i)
            if not m_items:
                menu_groups[index] = None
        menu_group.update({'menu_groups': list(
            [_f for _f in menu_groups if _f])})
        return menu_group

    def enable_mod(self, mod_name):
        if mod_name == '':
            return True
        l_mod = mod_name.split(';')
        for m in l_mod:
            if m in ('system',) and self.mod_name in ('system',):
                return True
            if m in ('person',) and self.mod_name in ('person',):
                return True
            if m in ('staff_meeting',) and self.mod_name in ('staff_meeting',):
                return True
            if m in ('staff_visitor',) and self.mod_name in ('staff_visitor',):
                return True
            if m == self.mod_name and m in settings.ENABLED_MOD and m in settings.SALE_MODULE:
                return True
            if 'system-' in m and m[7:] in settings.SALE_MODULE:
                return True
        return False

    def get_sub_menu(self, mod_name):
        self.mod_name = mod_name
        self.default_access = None
        sub_menu_template = """
            <div class=\"layui-side-scroll\">
                <ul class=\"layui-nav layui-nav-tree layui-inline\" lay-filter=\"admin-nav\" style=\"margin-right: 10px;\">
                    %s
                </ul>
            </div>
        """
        sub_menu_li = """
            <li class=\"layui-nav-item %s\">
                <a href=\"javascript:void(0);\">%s</a>
                <dl class=\"layui-nav-child\">
                    %s
                </d1>
            </li>
        """
        system_menus = self.system_menus
        menus = []
        module_menu = system_menus.get(mod_name, None)
        if not module_menu:
            return ('', '')
        menu_groups = module_menu.get('menu_groups', None)
        if not menu_groups:
            return ('', '')
        for menu_group in menu_groups:
            group_menus = menu_group['menus']
            (group_menu, selected) = self.get_group_menu(group_menus)
            cls = ''
            if selected:
                cls = 'layui-nav-itemed'
            if group_menu:
                menus.append(smart_str(sub_menu_li %
                             (cls, menu_group['verbose_name'], group_menu)))
        html = ''.join(menus)
        return (sub_menu_template % html, self.default_access)

    def get_group_menu(self, group_menus):
        sub_menu_template = """
            <dd class=\"%s\"><a id='%s' href=\"javascript:void(0);\" %s >%s</a></dd>
        """
        menus = []
        selected = False
        for m in group_menus:
            on_click = ''
            _url = m.get('url', None)
            cls = ''
            if _url:
                if not self.default_access:
                    self.default_access = _url
                    cls = 'layui-this'
                    selected = True
                on_click = 'onclick=menuClick("{0}",this);'.format(_url)
            menus.append(smart_str(sub_menu_template % (cls, '%s_%s' % (
                self.mod_name, m['model_name']), on_click, m['verbose_name'])))
        html = ''.join(menus)
        return (html, selected)

    def get_available_module(self):
        if not isinstance(self.request.user, get_user_model()):
            available_modules = {'staff', 'staff_payroll',
                                 'staff_meeting', 'staff_visitor'}
        else:
            available_modules = {
                t['id'] for t in settings.STANDARD_MODULES if not t['id'].startswith('staff')}
        return available_modules

    def get_modules(self):
        module_menu = """
           <li class=\"layui-nav-item %(cls)s\">
              <div class=\"menu_module\">
                <a href=\"javascript:void(0);\" rel='%(module_url)s'  >%(verbose_name)s</a>
              </div>
           </li>
        """
        available_modules = self.get_available_module()
        menus = []
        for m in self.standard_modules:
            module_name = m['id']
            if module_name not in available_modules:
                continue
            cls = ''
            if module_name == self.mod_name:
                cls = 'this'
            try:
                module_url = reverse('biotime:app_list', params={
                                     'app_label': module_name})
            except Exception:
                module_url = ''
            menu_li = module_menu % {
                'cls': cls, 'module_url': module_url, 'verbose_name': '{0}'.format(m['caption'])}
            append = False
            module_sub_menu = self.get_sub_menu(module_name)
            if module_sub_menu:
                append = True
            if append:
                menus.append(menu_li)
        html = ''.join(menus)
        return html

    def get_sub_menus(self, module_name, pin_tabs):
        sub_menus = []
        if pin_tabs is None:
            pin_tabs = []
        menu_groups = self.system_menus[module_name]
        groups = menu_groups.get('menu_groups', [])
        for group in groups:
            if not group.get('visible', True):
                continue
            menus = group.get('menus', [])
            menu_group = {'label': group.get(
                'verbose_name', ''), 'url': '', 'icon': group.get('icon', ''), 'menus': []}
            for _m in menus:
                if not _m.get('visible', True):
                    continue
                is_priority = _m.get('priority', False)
                url = _m.get('url', '')
                _detail = {'label': _m.get('verbose_name', ''), 'url': url, 'hex': url.encode(
                    'utf-8').hex(), 'priority': is_priority}
                if url in pin_tabs:
                    _detail.update(pin=True)
                menu_group['menus'].append(_detail)
            sub_menus.append(menu_group)
        return sub_menus

    def get_menus(self):
        try:
            pin_tabs = load_from_json(self.user.userprofile.pin_tabs, dict)
        except (ValueError, AttributeError):
            pin_tabs = {}
        menus = []
        available_modules = self.get_available_module()
        for m in self.standard_modules:
            module_name = m['id']
            if module_name not in available_modules:
                continue
            if module_name not in self.system_menus:
                continue
            app = {'label': m['caption'], 'url': '', 'app': module_name, 'groups': self.get_sub_menus(
                module_name, pin_tabs.get(module_name, None))}
            menus.append(app)
        return menus


'''
if enable_core and auth_settings.ENABLE_ATT and self.user.has_perm('accounts.enter_attendance_module'):
            from att import APP_NAME, get_menu
            self.att_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(self.att_menu, APP_NAME)
        if enable_contact and auth_settings.ENABLE_DEV and self.user.has_perm('accounts.enter_terminal_module'):
            from src.iclock import APP_NAME, get_menu
            self.terminal_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(self.terminal_menu, APP_NAME)
        if enable_application and auth_settings.ENABLE_ACC and self.user.has_perm('accounts.enter_access_module'):
            from acc import APP_NAME, get_menu
            self.access_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(self.access_menu, APP_NAME)
        if enable_visitor and auth_settings.ENABLE_VISITOR and self.user.has_perm('accounts.enter_visitor_module'):
            from visitor import APP_NAME, get_menu
            self.visitor_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(self.visitor_menu, APP_NAME)
        if enable_meeting and auth_settings.ENABLE_MEETING and self.user.has_perm('accounts.enter_meeting_module'):
            from meeting import APP_NAME, get_menu
            self.meeting_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(self.meeting_menu, APP_NAME)
        if enable_base and self.user.has_perm('accounts.enter_system_module'):
            from src.base import APP_NAME, get_menu
            self.system_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(self.system_menu, APP_NAME)
        if auth_settings.ENABLE_STAFF and self.user.has_perm('staff'):
            from staff import APP_NAME, get_menu
            self.staff_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(self.staff_menu, APP_NAME)
            if auth_settings.ENABLE_MEETING and self.user.has_perm('staff_meeting'):
                from staff_meeting import APP_NAME, get_menu
                self.staff_menu = get_menu(self.site.get_url)
                self.system_menus[APP_NAME] = self.filter_eligible_menu(self.staff_menu, APP_NAME)
            if auth_settings.ENABLE_VISITOR and self.user.has_perm('staff_visitor'):
                from staff_visitor import APP_NAME, get_menu
                self.staff_menu = get_menu(self.site.get_url)
                self.system_menus[APP_NAME] = self.filter_eligible_menu(self.staff_menu, APP_NAME)
        if enable_ep and auth_settings.ENABLE_EP and self.user.has_perm('accounts.enter_ep_module'):
            from ep import APP_NAME, get_menu
            self.ep_menu = get_menu(self.site.get_url)
            self.system_menus[APP_NAME] = self.filter_eligible_menu(self.ep_menu, APP_NAME)
'''
