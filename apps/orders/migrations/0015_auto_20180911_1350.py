# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20180908_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
