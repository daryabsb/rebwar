
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
        app_list = self.get_app_list(request)

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
            or ["admin/%s/app_index.html" % app_label, "admin/app_index.html"],
            context,
        )

z_site = ZAdminSite()