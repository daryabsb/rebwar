from django.contrib import admin
from src.accounts.models import DoctorProfile

from django.utils.translation import gettext as _

@admin.register(DoctorProfile)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'arabic_name', 'specialty', 'email')
    ordering = ('id', )