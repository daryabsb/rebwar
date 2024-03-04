from django.db import models
from src.core.modules import upload_image_file_path


class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(null=True, blank=True,
                              default='uploads/user/default-user-avatar.jpg',
                              upload_to=upload_image_file_path)

    def __str__(self):
        return self.name
