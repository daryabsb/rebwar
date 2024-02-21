from django.contrib import admin
from src.blogs.models import Blog, Like, Comment, Reply
# Register your models here.

admin.site.register(Blog)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Reply)
