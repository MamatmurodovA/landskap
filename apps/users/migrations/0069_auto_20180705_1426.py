# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0068_cafe_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='logo',
            field=models.ImageField(default='logo.png', upload_to='cafe'),
        ),
    ]
