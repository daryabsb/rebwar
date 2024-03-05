
from django.db import models
from django.urls import reverse
from src.accounts.managers import DoctorManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from src.core.modules import upload_image_file_path
from django.contrib.auth import get_user_model

User = get_user_model()


class DoctorProfile(models.Model):
    # Custom user model supports email instead of username
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='doctor')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    specialty = models.CharField(max_length=300)
    description = models.CharField(max_length=255)
    featured = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True,
                              default='uploads/user/default-user-avatar.png',
                              upload_to=upload_image_file_path)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('doctor_detail', kwargs={'pk': self.pk})


class DoctorLocation(models.Model):
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name="procedures")
    name = models.CharField(max_length=50)
    ordinal = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.doctor.name}: {self.name}"


@receiver(post_save, sender=DoctorProfile)
def create_user_for_doctor(sender, instance, created, **kwargs):
    """
    Signal handler to create a User for a new Doctor profile.
    """
    if created:
        #         # Set a default password for the user
        default_password = "defaultpassword@1234"

        user, user_created = User.objects.get_or_create(
            email=instance.email,
            defaults={
                'name': instance.name,
                'is_doctor': True
            }
        )

        user.set_password(default_password)
        user.save()

        # Assign the created user to the doctor's user field
        instance.user = user
        instance.save()
