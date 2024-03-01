"""
URL configuration for translation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.shortcuts import render

from blog.models import BlogPost

def index_view(request):
    return render(request, 'index.html')

from django.shortcuts import render
from django.utils.translation import gettext as _

def index_view(request):
    # You can add any context data you want to pass to the template here
    blog_posts = BlogPost.objects.all()  # Retrieve all blog posts
    return render(request, 'index.html', {'blog_posts': blog_posts})
   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('', index_view, name='home')
]

urlpatterns += i18n_patterns(
    # ... your translatable url patterns ...
    path('set_language/', set_language, name='set_language'),
)
