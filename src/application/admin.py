from django.contrib import admin
from src.application.models import Application
from modeltranslation.admin import TranslationAdmin


admin.site.register(Application, TranslationAdmin)
