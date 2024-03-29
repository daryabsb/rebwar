from modeltranslation.translator import register, TranslationOptions
from src.core.models import (
    Slide, Service, Treatment, Condition, Procedure, Testimonial,
    Menu, SectionContent, About, Journey, JourneyDetail)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'action',)
    # fallback_languages = {'default': ('ku', 'ar')}
    # fallback_values = _('-- sorry, no translation provided --')


@register(Slide)
class SlideTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    # fallback_languages = {'default': ('ku', 'ar')}
    # fallback_values = _('-- sorry, no translation provided --')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'detailed_description')


@register(Treatment)
class TreatmentTranslationOptions(TranslationOptions):
    fields = ('title', 'conditions_description', 'procedure_description')


@register(Condition)
class ConditionTranslationOptions(TranslationOptions):
    fields = ('text','description')


@register(Procedure)
class ProcedureTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    # fields = ('name')
    fields = ('name',)


@register(SectionContent)
class SectionContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Journey)
class JourneyTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(JourneyDetail)
class JourneyDetailTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('text',)
