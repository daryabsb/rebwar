"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings

from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language


from django.conf.urls.static import static
from django.urls import path, include

from src.app import views
from src.accounts.api.views import create_patient

urlpatterns = [
    path('', views.home_view, name='index'),
    path('admin/', admin.site.urls),
    path('about/', views.about_view, name='about'),
    path('contact-us/', views.contact_view, name='contact-us'),
    path('contact-us/', views.contact_view, name='contact-us'),
    path('doctors/', include('src.accounts.urls')),
    path('blogs/', include('src.blogs.urls')),
    path('services/', views.services_view, name='services'),
    path('services/<int:id>/', views.services_detail_view, name='services-detail'),
    path('api/create_patient/', create_patient, name='create_patient'),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += i18n_patterns(
    # ... your translatable url patterns ...
    path('set_language/', set_language, name='set_language'),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)