# Generated by Django 4.1.13 on 2024-02-20 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_service_description_service_detailed_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('conditions_description', models.TextField(blank=True, null=True)),
                ('procedure_description', models.TextField(blank=True, null=True)),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='treatment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='core.treatment')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='core.treatment')),
            ],
        ),
    ]