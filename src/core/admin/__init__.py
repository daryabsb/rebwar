from django.contrib import admin
from src.core.models import (Slide, Service, Journey, JourneyDetail, About,
                             Treatment, Condition, Procedure, Menu)
from modeltranslation.admin import TranslationAdmin
# Register your models here.


admin.site.register(Slide, TranslationAdmin)
admin.site.register(Journey)
admin.site.register(JourneyDetail)
admin.site.register(About)

admin.site.register(Service, TranslationAdmin)
admin.site.register(Treatment, TranslationAdmin)
admin.site.register(Condition, TranslationAdmin)
admin.site.register(Procedure, TranslationAdmin)

admin.site.register(Menu, TranslationAdmin)
