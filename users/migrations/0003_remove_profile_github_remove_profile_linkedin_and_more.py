# Generated by Django 5.0.6 on 2024-05-19 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='github',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='website',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='youtube',
        ),
    ]
