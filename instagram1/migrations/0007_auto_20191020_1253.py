# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-20 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram1', '0006_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
