# Generated by Django 5.0.2 on 2024-03-06 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_titlechoice_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('description_en', models.CharField(max_length=50, null=True)),
                ('description_ar', models.CharField(max_length=50, null=True)),
                ('description_ckb', models.CharField(max_length=50, null=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules', to='accounts.doctorprofile')),
            ],
        ),
    ]