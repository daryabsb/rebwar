# Generated by Django 5.0.2 on 2024-03-18 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_treatment_conditions_desc_treatment_procedure_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='conditions_desc',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='procedure_desc',
        ),
    ]
