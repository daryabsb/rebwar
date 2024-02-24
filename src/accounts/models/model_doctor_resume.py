from django.db import models

from src.accounts.models import DoctorProfile


class DoctorResume(models.Model):
    # Custom user model supports email instead of username
    doctor = models.OneToOneField(
        DoctorProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='resume')
