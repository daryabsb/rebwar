# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from src.blogs.models import Blog, Comment, Reply, Like
from .serializers import BlogSerializer, CommentSerializer, ReplySerializer, LikeSerializer


@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment_list(request, blog_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(blog_id=blog_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog_id=blog_id, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def like_list(request, content_type, object_id):
    from django.contrib.contenttypes.models import ContentType
    from django.http import Http404
    try:
        # Get the ContentType for the specified model
        content_type_model = ContentType.objects.get(model=content_type)
    except ContentType.DoesNotExist:
        raise Http404("Invalid content type")

    if request.method == 'GET':
        likes = Like.objects.filter(
            content_type=content_type_model, object_id=object_id)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Use the correct content type ID in the serializer data
        serializer_data = request.data.copy()
        serializer_data['content_type'] = content_type_model.id

        serializer = LikeSerializer(data=serializer_data)
        if serializer.is_valid():
            serializer.save(object_id=object_id, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
