# Generated by Django 5.0.2 on 2024-03-05 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_patient_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='city',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='country',
        ),
    ]