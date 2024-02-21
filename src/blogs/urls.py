from django.urls import path, include
from .views import BlogListView, BlogDetailView
# CommentDetailView, ReplyDetailView, LikeView

urlpatterns = [
    path('api/', include('src.blogs.api.urls')),
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    # path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    # path('replies/<int:pk>/', ReplyDetailView.as_view(), name='reply_detail'),
    # path('like/', LikeView.as_view(), name='like'),
]
