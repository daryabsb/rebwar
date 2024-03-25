from django.contrib import admin
from src.contact.models import Contact
from modeltranslation.admin import TranslationAdmin
from src.xadmin import z_site


admin.site.register(Contact, TranslationAdmin)

z_site.register(Contact, TranslationAdmin)