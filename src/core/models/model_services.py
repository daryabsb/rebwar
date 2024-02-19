from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title
