# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPage', '0004_user_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]
