# Generated by Django 4.0.4 on 2022-07-21 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_job_experience_job_salary_job_vacancy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='title',
            new_name='Title',
        ),
    ]
