from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from tinymce import models as tinymce_models
from django.urls import reverse
from src.core.modules import upload_image_file_path
from src.app.const import LANGUAGES_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}"


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    handle = models.SlugField()
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=50)
    language = models.CharField(
        max_length=3, default='en', choices=LANGUAGES_CHOICES, unique=True)
    short_description = tinymce_models.HTMLField(blank=True, null=True)
    content = tinymce_models.HTMLField()
    likes = GenericRelation(Like, related_query_name='blog_likes')
    image = models.ImageField(null=True, blank=True,
                              default='uploads/user/default-user-avatar.png',
                              upload_to=upload_image_file_path)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like, related_query_name='comment_likes')

    def __str__(self):
        return f'Comment by {self.user.name} on {self.blog.title}'


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like, related_query_name='reply_likes')

    def __str__(self):
        return f'Reply by {self.user.name} on {self.comment.blog.title}'
