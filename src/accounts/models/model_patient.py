from django.db import models
from django_countries.fields import CountryField
from django_countries import countries
# from src.accounts.models import City
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from src.core.modules import upload_image_file_path
from django.contrib.auth import get_user_model

User = get_user_model()


class Patient(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='patient')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=15, choices=countries, default='iq')
    city = models.CharField(max_length=35)
    # city = models.ForeignKey(
    #     "City", on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='uploads/user/default-user-avatar.jpg',
                              upload_to=upload_image_file_path)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('doctor_detail', kwargs={'pk': self.pk})


@receiver(post_save, sender=Patient)
def create_user_for_doctor(sender, instance, created, **kwargs):
    """
    Signal handler to create a User for a new Patient profile.
    """
    if created:
        #         # Set a default password for the user
        default_password = "defaultpassword@1234"

        user, user_created = User.objects.get_or_create(
            email=instance.email,
            defaults={
                'name': instance.name,
                'is_patient': True
            }
        )

        user.set_password(default_password)
        user.save()

        # Assign the created user to the doctor's user field
        instance.user = user
        instance.save()
