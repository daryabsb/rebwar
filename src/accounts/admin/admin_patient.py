from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from src.accounts.models import Patient, City


@admin.register(Patient)
class PatientAdmin(TranslationAdmin):
    list_display = ('name', 'email', 'country', 'city')  #
    list_filter = ('country',)
    # search_fields = ('name', 'email', 'city__name')
    show_facets = admin.ShowFacets.ALWAYS

    fieldsets = (
        (_('Personal Information'), {
            'fields': ('name', 'email', 'user')
        }),
        (_('Location Information'), {
            'fields': ('country', 'city')
        }),
        (_('Profile Picture'), {
            'fields': ('image',),
        }),
    )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


# admin.site.register(Patient, PatientAdmin)
