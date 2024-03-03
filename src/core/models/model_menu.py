from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Menu(models.Model):
    ordinal = models.SmallIntegerField()
    name = models.CharField(max_length=255)
    link = models.CharField(blank=True, null=True)
    parent_menu = models.ForeignKey(
        'self', null=True, blank=True, related_name='submenus', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
