from modeltranslation.translator import register, TranslationOptions
from src.accounts.models import DoctorProfile, Patient, DoctorLocation
from django.utils.translation import gettext as _


@register(DoctorProfile)
class DoctorProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'specialty', 'description')
    # fallback_languages = {'default': ('ku', 'ar')}
    # fallback_values = _('-- sorry, no translation provided --')


@register(Patient)
class PatientTranslationOptions(TranslationOptions):
    fields = ('name',)
    fallback_languages = {'default': ('ckb', 'ar')}


@register(DoctorLocation)
class DoctorLocationTranslationOptions(TranslationOptions):
    fields = ('name',)
    fallback_languages = {'default': ('ckb', 'ar')}
