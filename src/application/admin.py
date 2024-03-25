from django.contrib import admin
from src.application.models import Application
from modeltranslation.admin import TranslationAdmin

from src.xadmin import z_site


admin.site.register(Application, TranslationAdmin)

z_site.register(Application, TranslationAdmin)
