# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 14:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='owner',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
