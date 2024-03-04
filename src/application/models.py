from django.db import models
from src.core.modules import upload_image_file_path
from django.contrib.auth import get_user_model

User = get_user_model()


class Application(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name='globals')
    key = models.CharField(max_length=50, unique=True)
    value = models.TextField()

    def __str__(self):
        return f"{self.key}"
