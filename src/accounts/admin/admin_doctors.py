from django.contrib import admin
from django.db import models
from django import forms
from tinymce.widgets import TinyMCE
from modeltranslation.admin import TranslationAdmin
from src.accounts.models import (DoctorProfile, DoctorLocation,
                                 DoctorResume, TitleChoice, DoctorSchedule,
                                 )


class DoctorProfileAdminForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = '__all__'
        widgets = {
            'journey': TinyMCE(attrs={'cols': 100, 'rows': 30})
        }

@admin.register(DoctorProfile)
class DoctorAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'specialty', 'email')
    ordering = ('id', )
    form = DoctorProfileAdminForm
 
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(DoctorLocation, TranslationAdmin)
admin.site.register(TitleChoice, TranslationAdmin)
admin.site.register(DoctorResume, TranslationAdmin)
admin.site.register(DoctorSchedule, TranslationAdmin)
