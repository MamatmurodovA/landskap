# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0122_user_is_can_reject'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafegeneralsettings',
            name='tax',
            field=models.IntegerField(default=0),
        ),
    ]