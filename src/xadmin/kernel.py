

from src.xadmin.mixins import ModelMixinEssential,ModelMixinAction, ModelMixinExtend, ModelMixinExport
from django.contrib.admin.options import ModelAdmin
from src.xadmin.action import GeneralActionDelete, GeneralActionNew


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
    add_form_template = None
    change_form_template = None
    detail_form_template = None
    export_fields_dict = {}
    export_mimes = {
      'xlsx': 'application/vnd.ms-excel',
      'xls': 'application/vnd.ms-excel',
      'pdf': 'application/pdf',
      'csv': 'application/download',
      'txt': 'text/plain'}
    m2m_url_handler = {}
    search_form = None
