from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_groups')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)