# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-15 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPage', '0011_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_id',
            field=models.CharField(default='NULL', max_length=30),
        ),
    ]
