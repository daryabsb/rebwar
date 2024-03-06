from modeltranslation.translator import register, TranslationOptions
from src.accounts.models import (DoctorProfile, Patient, DoctorLocation,
                                 DoctorResume, TitleChoice, DoctorSchedule,
                                 )
from django.utils.translation import gettext as _


@register(DoctorProfile)
class DoctorProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'field', 'description', 'journey')
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


@register(TitleChoice)
class TitleChoiceTranslationOptions(TranslationOptions):
    fields = ('display',)
    fallback_languages = {'default': ('ckb', 'ar')}


@register(DoctorResume)
class DoctorResumeTranslationOptions(TranslationOptions):
    fields = ('description',)
    fallback_languages = {'default': ('ckb', 'ar')}


@register(DoctorSchedule)
class DoctorScheduleTranslationOptions(TranslationOptions):
    fields = ('description',)
    fallback_languages = {'default': ('ckb', 'ar')}
