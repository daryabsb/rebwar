from django.contrib import admin
from django.utils.translation import gettext as _
from src.core.models import (Slide, Service, Journey, JourneyDetail, About,
                             Treatment, Condition, Procedure, Menu, SectionContent)
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
# Register your models here.


class AboutAdmin(TranslationAdmin):
    # Your admin configuration here
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(About, AboutAdmin)

admin.site.register(Slide, TranslationAdmin)
admin.site.register(Journey)
admin.site.register(JourneyDetail)

admin.site.register(Service, TranslationAdmin)
admin.site.register(Treatment, TranslationAdmin)
admin.site.register(Condition, TranslationAdmin)
admin.site.register(Procedure, TranslationAdmin)

admin.site.register(Menu, TranslationAdmin)


class SectionContentInline(TranslationTabularInline):
    model = SectionContent
    extra = 1


class SectionContentAdmin(TranslationAdmin):
    inlines = [SectionContentInline, ]

    list_display = ('content_type', 'object_id', 'title', 'description')
    search_fields = ('title', 'description')

    fieldsets = (
        (_('Content Details'), {
            'fields': ('content_type', 'object_id', 'title', 'description'),
        }),
        (_('Translated Content'), {
            'fields': ('title_translated', 'description_translated'),
            'classes': ('collapse',),
        }),
    )


# Register the SectionContent model with the custom admin
admin.site.register(SectionContent, SectionContentAdmin)
