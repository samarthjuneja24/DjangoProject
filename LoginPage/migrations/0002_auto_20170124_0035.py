# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
