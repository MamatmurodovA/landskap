# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-24 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0100_auto_20180913_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weektime',
            name='cafe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='week_time', to='users.Cafe'),
        ),
    ]
