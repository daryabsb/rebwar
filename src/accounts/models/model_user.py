from django.contrib import auth
from django.db import models
from src.accounts.managers import UserManager
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import AbstractBaseUser, _user_has_perm
from django.contrib.auth.models import PermissionsMixin
from src.core.modules import upload_image_file_path


def _user_has_model_op_perms(user, app_label, model_name):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_model_op_perms'):
            continue
        try:
            if backend.has_model_op_perms(user, app_label, model_name):
                return True
        except PermissionDenied:
            return False

    return False


class User(PermissionsMixin, AbstractBaseUser):
    # Custom user model supports email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    pin_tabs = models.TextField(default='', blank=True)
    preferences = models.TextField(default='', blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='uploads/user/default-user-avatar.png',
                              upload_to=upload_image_file_path)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_preferences(self, key=None, default=None):
        from src.xadmin.utils import load_from_json
        if not getattr(self, '_saved_preferences', None):
            saved = self.preferences
            decode_saved = load_from_json(saved, dict)
            self._saved_preferences = decode_saved
        if key is not None:
            return self._saved_preferences.get(key, default)
        return self._saved_preferences

    def set_preferences(self, new_attrs):
        import json
        saved_preference = self.get_preferences()
        saved_preference.update(new_attrs)
        self.preferences = json.dumps(saved_preference)

    class Meta(object):
        default_permissions = ()
        permissions = (('enter_system_module', 'can_enter_menu_system_module'), ('enter_accounts_module', 'can_enter_accounts_module'),
                       ('enter_contact_module', 'can_enter_contact_module'), (
                           'enter_core_module', 'can_enter_core_module'),
                       ('enter_application_module', 'can_enter_application_module'), (
                           'enter_access_module', 'can_enter_access_module'),
                       ('enter_blogs_module', 'can_enter_blogs_module'))

    def has_perm(self, perm, obj=None):
        if self.is_active:
            if self.is_superuser:
                return True
        return _user_has_perm(self, perm, obj)

    def has_model_op_perms(self, app_label, model_name):
        """
        Returns True if the user has any operation permissions in the given app label.
        Uses pretty much the same logic as has_perm, above.
        """
        if self.is_active:
            if self.is_superuser:
                return True
        return _user_has_model_op_perms(self, app_label, model_name)
