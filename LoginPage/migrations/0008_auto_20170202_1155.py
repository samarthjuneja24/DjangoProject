# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginPage', '0007_auto_20170201_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
