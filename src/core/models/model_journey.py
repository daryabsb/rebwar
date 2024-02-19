from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Journey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class JourneyDetail(models.Model):
    journey = models.ForeignKey(
        Journey, on_delete=models.CASCADE, related_name="journey_details")
    text = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.journey.title}: {self.text}"
