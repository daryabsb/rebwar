from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)