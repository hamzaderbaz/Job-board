# Generated by Django 4.0.4 on 2022-09-29 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0024_job_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='image',
        ),
    ]
