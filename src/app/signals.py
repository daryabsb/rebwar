

from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from src.blogs.models import Blog

def add_slug_to_model(sender, instance, *args, **kwargs):
    # if instance and not instance.handle:
    handle = slugify(instance.title)
    random_string = get_random_string(length=8)
    instance.handle = handle + "-" + random_string


pre_save.connect(add_slug_to_model, sender=Blog)