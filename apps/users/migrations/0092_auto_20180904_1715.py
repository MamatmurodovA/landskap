# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-04 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0091_auto_20180904_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Cafe owner'), (2, 'Simple user')], default=2),
        ),
    ]
