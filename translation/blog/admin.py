from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import BlogPost

# Register your models here.


@admin.register(BlogPost)
class YourModelAdmin(TranslationAdmin):
    pass