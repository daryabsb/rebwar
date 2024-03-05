from django.db import models
from django.urls import reverse
from src.core.modules import upload_image_file_path
from django.contrib.auth import get_user_model

User = get_user_model()


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True, blank=True)
    detailed_description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='uploads/user/default-user-avatar.png',
                              upload_to=upload_image_file_path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services-detail', kwargs={'id': self.pk})


class Treatment(models.Model):
    service = models.OneToOneField(
        Service, on_delete=models.CASCADE, related_name='treatment')
    title = models.CharField(max_length=100)
    conditions_description = models.TextField(null=True, blank=True)
    procedure_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.service.title} treatment"


class Condition(models.Model):
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, related_name="conditions")
    text = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.treatment.title}: {self.text}"


class Procedure(models.Model):
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, related_name="procedures")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    ordinal = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['ordinal']

    def __str__(self):
        return f"{self.treatment.title}: {self.title}: {self.description}"

