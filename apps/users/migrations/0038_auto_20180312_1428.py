# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-12 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_remove_company_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='position',
            new_name='location',
        ),
    ]
