# Generated by Django 4.1.13 on 2024-02-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_treatment_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedure',
            name='ordinal',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]