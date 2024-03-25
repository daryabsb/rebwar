from django.contrib import admin
from src.xadmin import z_site, register
from src.xadmin.kernel import ZModelAdmin
from django.db import models
from django import forms
from tinymce.widgets import TinyMCE
from modeltranslation.admin import TranslationAdmin
from src.accounts.models import (DoctorProfile, DoctorLocation,
                                 DoctorResume, TitleChoice, DoctorSchedule,
                                 )
from src.accounts.widgets import InputFieldWidget
submit_row
class DoctorProfileAdminForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
            'field': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'journey': TinyMCE(attrs={'cols': 10, 'rows': 30}),
            'content': TinyMCE(attrs={'cols': 40, 'rows': 30}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input form-control-sm'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
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

@register(DoctorProfile)
class DoctorAdmin(ZModelAdmin, TranslationAdmin):
    list_display = ('id', 'name', 'specialty', 'email')
    ordering = ('id', )
    change_form_template = "xadmin/accounts/x_doctor_change_form.html"
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

# z_site.register(DoctorProfile, ZModelAdmin)
z_site.register(DoctorLocation, TranslationAdmin)
z_site.register(TitleChoice, TranslationAdmin)
z_site.register(DoctorResume, TranslationAdmin)
z_site.register(DoctorSchedule, TranslationAdmin)