# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-06 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0110_auto_20181006_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freeitem',
            name='cafe',
        ),
        migrations.AddField(
            model_name='freeitem',
            name='root_cafe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exchanged_product', to='users.CafeGeneralSettings'),
        ),
    ]
