# Generated by Django 5.0.2 on 2024-03-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_testimonial_text_ar_testimonial_text_ckb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='text_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='text_ckb',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='text_en',
            field=models.CharField(max_length=200, null=True),
        ),
    ]