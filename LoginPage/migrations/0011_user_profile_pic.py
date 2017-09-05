# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPage', '0010_remove_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='', height_field=200, upload_to='Documents/%Y/%m/%d', width_field=200),
        ),
    ]