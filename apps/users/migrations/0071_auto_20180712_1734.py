# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-12 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0070_auto_20180705_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='city',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='cafe',
            name='second_address',
            field=models.TextField(blank=True, null=True, verbose_name='Address 2'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='state',
            field=localflavor.us.models.USStateField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address 1'),
        ),
    ]
