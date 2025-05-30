from django.db import models
from src.core.modules import upload_image_file_path
from django.contrib.auth import get_user_model

User = get_user_model()


class Slide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True,
                              default='uploads/user/default-user-avatar.png',
                              upload_to=upload_image_file_path)
    def __str__(self):
        return self.title