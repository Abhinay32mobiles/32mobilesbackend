# Generated by Django 3.2.1 on 2023-10-22 12:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('email_reply', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SimplifiedUserProfile',
            new_name='UserProfile',
        ),
    ]
