# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-19 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0121_auto_20181026_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_can_reject',
            field=models.BooleanField(default=False, verbose_name='Reject'),
        ),
    ]