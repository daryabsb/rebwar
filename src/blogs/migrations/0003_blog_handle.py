# Generated by Django 5.0.2 on 2024-03-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blog_content_alter_blog_content_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='handle',
            field=models.SlugField(default='handle'),
            preserve_default=False,
        ),
    ]
