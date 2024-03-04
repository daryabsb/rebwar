from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from src.accounts.models import DoctorProfile

from django.utils.translation import gettext as _

@admin.register(DoctorProfile)
class DoctorAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'specialty', 'email')
    ordering = ('id', )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


# Register your models here.


# @admin.register(DoctorProfile)
# class YourModelAdmin(DoctorAdmin, TranslationAdmin):
