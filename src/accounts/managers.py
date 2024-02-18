from django.contrib.auth.models import BaseUserManager
from django.db import models
# from src.core.modules import generate_activation_code


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, name=None, terms=False,
                    **extra_fields):
        # Creates and save a new user
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.name = name
        user.terms = terms
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Creates and save a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class DoctorManager(models.Manager):
    def create_doctor(self, email, name, specialty, description, featured):
        from django.contrib.auth import get_user_model

        User = get_user_model()
        # Set a default password for the user
        default_password = "defaultpassword@1234"

        # Get or create a User with the provided email
        user = User.objects.get(email=email)

        # If the user already exists, update the username field
        if not user:
            user = User.objects.create_user(
                email, default_password, name
            )

        # Create the Doctor instance without the user field
        doctor = self.create(
            user=user,
            name=name,
            email=email,
            specialty=specialty,
            description=description,
            featured=featured
        )

        return doctor
