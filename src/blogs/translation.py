from modeltranslation.translator import register, TranslationOptions
from src.blogs.models import (Blog,)


@register(Blog)
class DoctorProfileTranslationOptions(TranslationOptions):
    fields = ('title', 'subject', 'short_description', 'content')
    # fallback_languages = {'default': ('ku', 'ar')}
    # fallback_values = _('-- sorry, no translation provided --')
