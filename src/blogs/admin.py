from django.contrib import admin
from src.blogs.models import Blog, Like, Comment, Reply
from modeltranslation.admin import TranslationAdmin
# Register your models here.

admin.site.register(Blog, TranslationAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Reply)
