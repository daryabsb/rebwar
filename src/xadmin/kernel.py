

import copy
from src.xadmin.mixins import ModelMixinEssential,ModelMixinAction, ModelMixinExtend, ModelMixinExport
from django.contrib.admin.options import ModelAdmin
from src.xadmin.action import GeneralActionDelete, GeneralActionNew

from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.contrib.admin.options import get_content_type_for_model
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters

from django import forms
# from django.contrib.admin import widgets
from django.db import models, router, transaction

from src.xadmin import helpers

IS_POPUP_VAR = "_popup"
TO_FIELD_VAR = "_to_field"

HORIZONTAL, VERTICAL = 1, 2


# FORMFIELD_FOR_DBFIELD_DEFAULTS = {
#     models.DateTimeField: {
#         "form_class": forms.SplitDateTimeField,
#         "widget": widgets.AdminSplitDateTime,
#     },
#     models.DateField: {"widget": widgets.AdminDateWidget},
#     models.TimeField: {"widget": widgets.AdminTimeWidget},
#     models.TextField: {"widget": widgets.AdminTextareaWidget},
#     models.URLField: {"widget": widgets.AdminURLFieldWidget},
#     models.IntegerField: {"widget": widgets.AdminIntegerFieldWidget},
#     models.BigIntegerField: {"widget": widgets.AdminBigIntegerFieldWidget},
#     models.CharField: {"widget": widgets.AdminTextInputWidget},
#     models.ImageField: {"widget": widgets.AdminFileWidget},
#     models.FileField: {"widget": widgets.AdminFileWidget},
#     models.EmailField: {"widget": widgets.AdminEmailInputWidget},
#     models.UUIDField: {"widget": widgets.AdminUUIDInputWidget},
# }


class ZModelAdmin(ModelAdmin, ModelMixinEssential, ModelMixinAction, ModelMixinExtend, ModelMixinExport):
    actions = [GeneralActionNew, GeneralActionDelete]
    action_sets = None
    actions_disabled = []
    checkbox_name = 'id'
    sort_fields = []
    # hidden_fields = config.WDMS_HIDDEN
    non_display_fields = ()
    empty_value_display = '-'
    grid_template = None
    
    # Custom templates (designed to be over-ridden in subclasses)
    add_form_template = "xadmin/xchange_form.html"
    change_form_template = "xadmin/xchange_form.html"
    change_list_template = "xadmin/xchange_list.html"
    delete_confirmation_template = "xadmin/xdelete_confirmation.html"
    delete_selected_confirmation_template = None
    object_history_template = "xadmin/xobject_history.html"
    popup_response_template = None

        # Actions
    actions = ()
    action_form = helpers.XActionForm
    actions_on_top = True
    actions_on_bottom = False

    is_app_list=True

    export_fields_dict = {}
    export_mimes = {
      'xlsx': 'application/vnd.ms-excel',
      'xls': 'application/vnd.ms-excel',
      'pdf': 'application/pdf',
      'csv': 'application/download',
      'txt': 'text/plain'}
    m2m_url_handler = {}
    search_form = None
