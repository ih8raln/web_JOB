# Generated by Django 5.0.6 on 2024-06-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_kind_of_job_alter_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
