from modeltranslation.translator import register, TranslationOptions
from src.accounts.models import DoctorProfile
from django.utils.translation import gettext as _


@register(DoctorProfile)
class DoctorProfileTranslationOptions(TranslationOptions):
    fields = ('name', 'specialty', 'description')
    # fallback_languages = {'default': ('ku', 'ar')}
    # fallback_values = _('-- sorry, no translation provided --')
