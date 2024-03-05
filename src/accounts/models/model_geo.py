# yourapp/models.py
from django.db import models
from django_countries.fields import CountryField


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    asciiname = models.CharField(max_length=200)
    alternatenames = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = CountryField()
    population = models.BigIntegerField()
    timezone = models.CharField(max_length=40)
    modification_date = models.DateField()

    def __str__(self):
        return f"{self.name}, {self.country}"
