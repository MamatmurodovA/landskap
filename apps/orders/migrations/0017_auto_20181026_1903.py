# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20180927_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, choices=[('new', 'New'), ('ready', 'Ready')], default='new', max_length=60),
        ),
    ]
