# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-28 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPage', '0003_auto_20170128_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
