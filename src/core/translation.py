from modeltranslation.translator import register, TranslationOptions
from src.core.models import Slide, Service
from django.utils.translation import gettext as _


@register(Slide)
class SlideTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    # fallback_languages = {'default': ('ku', 'ar')}
    # fallback_values = _('-- sorry, no translation provided --')


@register(Slide)
class SlideTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    # fallback_languages = {'default': ('ku', 'ar')}
    # fallback_values = _('-- sorry, no translation provided --')
