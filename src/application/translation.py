from modeltranslation.translator import register, TranslationOptions
from src.application.models import Application


@register(Application)
class ApplicationTranslationOptions(TranslationOptions):
    fields = ('value',)
