# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20180220_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_of_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='date of birthday'),
        ),
    ]
