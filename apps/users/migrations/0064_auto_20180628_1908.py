# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0063_auto_20180620_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Cafe owner'), (2, 'User')], default=2),
        ),
    ]
