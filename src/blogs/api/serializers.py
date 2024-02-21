# serializers.py

from rest_framework import serializers
from src.blogs.models import Blog, Comment, Reply, Like
from src.accounts.api.serializers import UserSerializer


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Reply
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
