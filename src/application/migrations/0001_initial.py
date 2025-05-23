# Generated by Django 5.0.2 on 2024-03-16 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, unique=True)),
                ('value', models.TextField()),
                ('value_en', models.TextField(null=True)),
                ('value_ar', models.TextField(null=True)),
                ('value_ckb', models.TextField(null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='globals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
