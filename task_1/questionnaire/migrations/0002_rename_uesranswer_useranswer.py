# Generated by Django 4.1.4 on 2022-12-09 09:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UesrAnswer',
            new_name='UserAnswer',
        ),
    ]