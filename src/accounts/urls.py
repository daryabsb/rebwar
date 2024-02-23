from django.urls import path, include
from .views import DoctorDetailView
# CommentDetailView, ReplyDetailView, LikeView

urlpatterns = [
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
]
