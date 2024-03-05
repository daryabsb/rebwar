from django.db import models
from src.core.modules import upload_image_file_path
from src.accounts.models import Patient
from django.contrib.auth import get_user_model

User = get_user_model()


class Testimonial(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.name}: {self.text}"
