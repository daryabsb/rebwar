
from django.conf import settings
from django.contrib.admin.sites import AdminSite, AlreadyRegistered

class ZAdminSite(AdminSite):
    login_template = 'xadmin/registration/login.html'
    # logout_template = 'layui/registration/logged_out.html'
    module = [i['id'] for i in settings.STANDARD_MODULES]
    # user_index_template = staff_index_template = 'dashboard.html'
    # app_index_template = 'admin_site.html'
    # password_change_template = 'admin/auth/user/change_password.html'
    # password_change_done_template = 'layui/registration/password_change_done.html'

    def __init__(self):
        super(ZAdminSite, self).__init__(name='zeneon')

z_site = ZAdminSite()