# Generated by Django 5.0.2 on 2024-03-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_procedure_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='description_ar',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='description_ckb',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='description_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_ckb',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]