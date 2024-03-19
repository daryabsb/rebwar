from django.contrib import admin
from src.blogs.models import Blog, Like, Comment, Reply
from modeltranslation.admin import TranslationAdmin
# Register your models here.


# admin.site.register(Blog, TranslationAdmin)


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('id', 'author', 'subject', 'title')
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



admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Reply)
