from modeltranslation.translator import register, TranslationOptions
from src.contact.models import Contact


@register(Contact)
class SlideTranslationOptions(TranslationOptions):
    fields = ('text',)
