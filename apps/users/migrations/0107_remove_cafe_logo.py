# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-01 15:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0106_auto_20181001_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='logo',
        ),
    ]