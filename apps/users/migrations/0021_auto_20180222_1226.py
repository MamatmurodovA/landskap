# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-22 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20180222_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='avatars/'),
        ),
    ]
