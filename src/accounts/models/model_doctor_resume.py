from django.db import models
from django.utils.translation import gettext as _
from src.accounts.models import DoctorProfile


class TitleChoice(models.Model):
    value = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.display


class DoctorResume(models.Model):

    doctor = models.ForeignKey(
        DoctorProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='resumes')
    title = models.ForeignKey(
        "TitleChoice", on_delete=models.CASCADE, related_name='titles')
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.title}: {self.description}"

    class Meta:
        ordering = ["id", 'title', 'created']


class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(
        DoctorProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='schedules')
    description = models.CharField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.doctor.name} - {self.description}: {self.start} - {self.end}"
