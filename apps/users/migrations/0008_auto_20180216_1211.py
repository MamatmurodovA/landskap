# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-16 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_company_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.IntegerField(choices=[(0, 'Blocked'), (1, 'Active'), (2, 'Pending')], max_length=2),
        ),
    ]
