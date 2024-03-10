# models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    preferred_locale = models.CharField(max_length=10)  # Assuming language codes like 'en', 'fr', etc.
    # Add other fields like city, country, long/lat, etc.

    def __str__(self):
        if self.user:
            return f"{self.user.name}: {self.ip_address}"
        return self.ip_address