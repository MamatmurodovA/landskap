# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-21 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_auto_20181221_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodifier',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
