
from functools import update_wrapper
from django.conf import settings
from django.contrib.admin.sites import AdminSite, AlreadyRegistered
from django.template.response import TemplateResponse
from django.views.decorators.common import no_append_slash
from django.urls import NoReverseMatch, Resolver404, resolve, reverse
from django.http import Http404, HttpResponsePermanentRedirect, HttpResponseRedirect


class ZAdminSite(AdminSite):
    site_title = 'Dr Rebwar Allaf | Orthopedic & Hans Clinic'
    site_header = 'Dr Rebwar Allaf | Orthopedic & Hans Clinic'
    index_title = 'Allaf Admin CMS'
    login_template = 'xadmin/registration/login.html'
    # logout_template = 'layui/registration/logged_out.html'
    module = [i['id'] for i in settings.STANDARD_MODULES]
    user_index_template = staff_index_template = 'dashboard.html'
    index_template = 'xadmin/xindex.html'
    app_index_template = 'xadmin/xapp_index.html'
    # password_change_template = 'admin/auth/user/change_password.html'
    # password_change_done_template = 'layui/registration/password_change_done.html'

    def __init__(self):
        super(ZAdminSite, self).__init__(name='zeneon')

    @no_append_slash
    def catch_all_view(self, request, url):
        if settings.APPEND_SLASH and not url.endswith("/"):
            urlconf = getattr(request, "urlconf", None)
            try:
                match = resolve("%s/" % request.path_info, urlconf)
            except Resolver404:
                pass
            else:
                if getattr(match.func, "should_append_slash", True):
                    return HttpResponsePermanentRedirect(
                        request.get_full_path(force_append_slash=True)
                    )
        raise Http404

    def index(self, request, extra_context=None):
        """
        Display the main admin index page, which lists all of the installed
        apps that have been registered in this site.
        """
        from src.xadmin.menu import MenuList

        app_list = self.get_app_list(request)
        print("We are here index!!")
        context = {
            **self.each_context(request),
            "title": self.index_title,
            "subtitle": None,
            "app_list": app_list,
            **(extra_context or {}),
        }

        request.current_app = self.name

        return TemplateResponse(
            request, self.index_template or "xadmin/xindex.html", context
        )

    def app_index(self, request, app_label, extra_context=None):
        from django.utils.translation import gettext as _

        app_list = self.get_app_list(request, app_label)

        if not app_list:
            raise Http404("The requested admin page does not exist.")

        context = {
            **self.each_context(request),
            "title": _("%(app)s administration") % {"app": app_list[0]["name"]},
            "subtitle": None,
            "app_list": app_list,
            "app_label": app_label,
            **(extra_context or {}),
        }

        request.current_app = self.name
        
        return TemplateResponse(
            request,
            self.app_index_template
            or [f"xadmin/{ app_label }/xapp_index.html", "xadmin/xapp_index.html"],
            context,
        )


    def my_custom_view(self, request):
        from django.http import HttpResponse
        from django.shortcuts import get_object_or_404, render, redirect
        
        context = {
            "message": "Successfully added your xadmin custom view!"
        }
        return render(request, 'xadmin/accounts/doctor_profile.html', context)

    def get_urls(self):
        from django.urls import path, include, re_path
        urls = super().get_urls()
        
        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)

            wrapper.admin_site = self
            return update_wrapper(wrapper, view)

        valid_app_labels = []
        for model, model_admin in self._registry.items():

            urls += [
                path(
                    "%s/%s/" % (model._meta.app_label, model._meta.model_name),
                    include(model_admin.urls),
                ),
            ]
            if model._meta.app_label not in valid_app_labels:
                valid_app_labels.append(model._meta.app_label)
        if valid_app_labels:
            regex = r"^(?P<app_label>" + "|".join(valid_app_labels) + ")/$"
            urls += [
                re_path(regex, wrap(self.app_index), name="app_list"),
            ]

        custom_urls = [
            path('my-custom-view/', self.admin_view(self.my_custom_view), name='my_custom_view'),
            path('accounts/doctor-profile/', wrap(self.app_index), name='accounts-doctor-profile'),
            # Add more custom URLs here
        ]
        return custom_urls + urls

    # def get_urls(self):
    #     from django.urls import path, include
    #     urls = super().get_urls()
    #     custom_urls = []
    #     valid_app_labels = set()

    #     for model, model_admin in self._registry.items():
    #         app_label = model._meta.app_label
    #         if app_label not in valid_app_labels:
    #             valid_app_labels.add(app_label)
    #             custom_urls.append(path(f'^{app_label}/$', self.app_index, name='app_list'))
    #         custom_urls.append(path(f'^{app_label}/{model._meta.model_name}/', include(model_admin.urls)))

    #     for app in settings.INSTALLED_APPS:
    #         if app.startswith('src.'):
    #             app_label = app.split('.')[-1]
    #             try:
    #                 custom_urls.append(path(f'^{app_label}/', include(f'{app}.urls')))
    #             except Exception as e:
    #                 import traceback
    #                 traceback.print_exc()

    #     return custom_urls + urls


z_site = ZAdminSite()




'''
    @never_cache
    def login(self, request, extra_context=None):
        """
        Displays the login form for the given HttpRequest.
        """
        import base64
        from mysite.authurls import logon
        from mysite.base.models import SecurityPolicy
        if request.method == 'GET':
            if self.has_permission(request):
                index_path = reverse('biotime:index', current_app=(self.name))
                return HttpResponseRedirect(index_path)
        policy = SecurityPolicy.default()
        lang_code = request.session[translation.LANGUAGE_SESSION_KEY] if translation.LANGUAGE_SESSION_KEY in request.session else settings.LANGUAGE_CODE
        if request.method == 'POST':
            login_user = request.POST.get('login_user', None)
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            remember_me_admin = request.POST.get('remember_me_admin', None)
            remember_me_employee = request.POST.get('remember_me_employee', None)
            if policy.security_code:
                verify_result = self.security_code_verify(request)
                if verify_result:
                    return HttpResponse(json.dumps({'ret':-8,  'message':str(verify_result)}))
            login_result = logon(request)
            if login_result.status_code == 200:
                account_info = {'username':login_user or user_name if remember_me_admin else '', 
                 'password':login_user or password if remember_me_admin else '', 
                 'empName':user_name if login_user and remember_me_employee else '', 
                 'empPwd':password if login_user and remember_me_employee else '', 
                 'remember_me_admin':'checked' if remember_me_admin and not login_user else '', 
                 'remember_me_employee':'checked' if remember_me_employee and login_user else ''}
                login_result.set_cookie((settings.ACCOUNT_COOKIE_NAME),
                  (base64.b64encode(json.dumps(account_info).encode())), max_age=(settings.ACCOUNT_COOKIE_AGE),
                  path=(settings.LANGUAGE_COOKIE_PATH),
                  domain=(settings.LANGUAGE_COOKIE_DOMAIN))
            return login_result
        from django.contrib.auth.views import LoginView
        from django.contrib.admin.forms import AdminAuthenticationForm
        from mysite.authorized import auth_settings
        context = dict((self.each_context(request)),
          LANGUAGES=(settings.LANGUAGES),
          LANGUAGE_CODE=lang_code,
          title=(_('Log in')),
          app_path=(request.get_full_path()),
          username=(request.user.get_username()),
          login_url=(self.get_url('login')))
        if REDIRECT_FIELD_NAME not in request.GET:
            if REDIRECT_FIELD_NAME not in request.POST:
                context[REDIRECT_FIELD_NAME] = reverse('admin:index', current_app=(self.name))
        context.update(extra_context or {})
        context['wdms_enable'] = settings.ENABLE_WDMS
        context['staff_enable'] = auth_settings.ENABLE_STAFF and not settings.ENABLE_WDMS
        context['security_code'] = policy.security_code
        defaults = {'extra_context':context, 
         'authentication_form':self.login_form or AdminAuthenticationForm, 
         'template_name':self.login_template or 'admin/login.html'}
        request.current_app = self.name
        if lang_code:
            if translation.check_for_language(lang_code):
                if hasattr(request, 'session'):
                    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
                translation.activate(lang_code)
        return (LoginView.as_view)(**defaults)(request)
'''