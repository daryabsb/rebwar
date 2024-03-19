from django.contrib import admin
from src.core.models import Service, Condition, Procedure, Treatment
from modeltranslation.admin import TranslationAdmin


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')
    ordering = ('id', )
 
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Treatment)
class TreatmentAdmin(TranslationAdmin):
    list_display = ('id', 'title')
    ordering = ('id', )
 
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Condition)
class ConditionAdmin(TranslationAdmin):
    list_display = ('id','treatment_title', 'text_en', 'text_ar', 'text_ckb',)
    ordering = ('treatment','id', )
    list_filter = ('treatment',)

    def treatment_title(self, obj):
        from django.forms import model_to_dict
        
        return obj.treatment.title
    treatment_title.short_description = 'treatment'
 
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Procedure)
class ProcedureAdmin(TranslationAdmin):
    list_display = ('ordinal','treatment_title', 'title_en', 'title_ar', 'title_ckb',)
    ordering = ('treatment','ordinal',)
    list_filter = ('treatment',)

    def treatment_title(self, obj):
        return obj.treatment.title
    treatment_title.short_description = 'treatment'
 
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }