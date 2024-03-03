from django.db import models
from src.core.modules import upload_image_file_path
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Contact(models.Model):
    CONTACT_CHOICES = (
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('address', 'Address'),
        ('phone', 'Phone'),
        ('social', 'Social'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name='contacts')
    category = models.CharField(
        max_length=20, choices=CONTACT_CHOICES, default='phone')
    text = models.CharField(max_length=500)
    is_primary = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
