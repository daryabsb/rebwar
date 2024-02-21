from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog, Comment, Reply


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/list.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the author of the current blog
        author = context['blog'].author

        # Get related posts by the same author (excluding the current post)
        related_posts = Blog.objects.filter(
            author=author).exclude(id=context['blog'].id)[:3]

        context['related_posts'] = related_posts
        return context
