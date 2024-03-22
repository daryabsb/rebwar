
from django.utils.translation import gettext_lazy as _




class ActionHandleError(Exception):
    __doc__ = 'Some errors happened during handle procedure of the requested action '


class ZKAction(object):
    verbose_name = None
    short_description = None
    help_txt = None
    action_form = None
    action_template = None
    action_icon = ''
    action_url = None
    confirmation = ''
    confirmation_times = 1
    action_confirm_password = False
    batch_select = False
    unique_object_required = False
    px_height = None
    px_width = None
    visible = True
    async_progress = False

    def __init__(self, request, admin=None, obj_ids=None):
        self.request = request
        self.admin = admin
        self.obj_ids = obj_ids
        self.valid_form = None

    def action(self, *args, **kwargs):
        raise NotImplementedError('subclasses of ZKAction must override action() method')



class ZModelAction(ZKAction):

    def __init__(self, request, admin=None, obj_ids=None):
        super(ZModelAction, self).__init__(request, admin, obj_ids)
        if self.obj_ids:
            cls = self.admin.model
            self.objects = cls.objects.filter(id__in=(self.obj_ids))
        else:
            self.objects = None




class GeneralActionDelete(ZModelAction):
    verbose_name = _('common_action_deleteSelectedRecord')
    short_description = _('common_action_deleteSelectedRecordDescription')
    help_txt = _('common_action_deleteSelectedRecordHelpTxt')
    action_icon = ''
    confirmation = _('are_you_sure_to_delete_the_selected')
    batch_select = True

    def action(self, **kwargs):
        from src.xadmin.utils import get_error_message
        from django.db import ProgrammingError
        from django.db import DatabaseError
        import django.core.cache as cache
        remove_non_permitted = kwargs.get('remove_denied', {})
        if len(remove_non_permitted) == len(self.objects):
            pass
        else:
            for k in getattr(self.admin, 'cache_keys', []):
                cache.delete(k)
                user = self.request.user
                if not user.is_superuser:
                    cache.delete('{key}_{user_id}'.format(key=k,
                      user_id=(user.id)))

        msg_list = []
        objects = []
        for obj in self.objects:
            try:
                obj_id = getattr(obj, 'id', getattr(obj, 'pk'))
                error_msg = remove_non_permitted.get(obj_id, None)
                if error_msg is not None:
                    msg_list.append(str(error_msg))
                    continue
                else:
                    objects.append('{obj}'.format(obj=obj))
                    obj.delete()
            except (ProgrammingError, DatabaseError) as e:
                try:
                    msg_list.append(get_error_message(e,
                      field=('<{}>'.format(obj.__class__.__name__))))
                finally:
                    e = None
                    del e

        if len(msg_list) > 0:
            raise ActionHandleError(';'.join(msg_list))
        else:
            return '|{obj}'.format(obj=(','.join(objects)))




class GeneralActionNew(ZModelAction):
    verbose_name = _('common_action_new')
    short_description = _('common_action_newDescription')
    help_txt = _('common_action_newHelpTxt')
    action_icon = ''
    action_url = '%s_%s_add'
    batch_select = False

    def action(self, **kwargs):
        pass