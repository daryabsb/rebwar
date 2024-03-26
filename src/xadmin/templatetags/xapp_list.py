from django.contrib.admin.views.main import (
    PAGE_VAR,
)
from django.template import Library
from src.xadmin import z_site
from django.contrib.admin import AdminSite

from .base import InclusionAdminNode

from django.utils.translation import gettext as _

register = Library()


def app_list(context):
    admin_site = AdminSite()
    apps = admin_site.get_app_list()
    for app in apps:
        print("app: ", app)
    return apps


@register.tag(name="app_list")
def app_list_tag(parser, token):
    return InclusionAdminNode(
        parser, token, func=app_list, template_name="x_doctor_change_form.html"
    )
