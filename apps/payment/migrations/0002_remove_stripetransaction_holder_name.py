# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-18 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stripetransaction',
            name='holder_name',
        ),
    ]
