# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-09 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20180309_1947'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='File',
        ),
    ]