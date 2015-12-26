# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 09:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='submitter',
            field=models.ForeignKey(default=6, on_delete=models.SET(4), to=settings.AUTH_USER_MODEL),
        ),
    ]