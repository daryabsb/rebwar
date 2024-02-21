# urls.py

from django.urls import path
from .views import blog_list, blog_detail, comment_list, like_list

urlpatterns = [
    path('list/', blog_list, name='blog-list'),
    path('<int:blog_id>/', blog_detail, name='blog-detail'),
    path('<int:blog_id>/comments/', comment_list, name='comment-list'),
    path('likes/<str:content_type>/<int:object_id>/',
         like_list, name='like-list'),
]
