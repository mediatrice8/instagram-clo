# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-19 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePhoto', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('bio', models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_date']},
        ),
    ]