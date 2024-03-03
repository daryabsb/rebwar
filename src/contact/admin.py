from django.contrib import admin
from src.contact.models import Contact
from modeltranslation.admin import TranslationAdmin


admin.site.register(Contact, TranslationAdmin)
