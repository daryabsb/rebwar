
from django.db import models
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

'''
from src.accounts.models import DoctorProfile as DF
d = DF(name='Rebwar A. Allaf',email='rebwar.allaf@gmail.com',description='This is our doctor',specialty='MD',featured=True)
d.save()
'''


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
