# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-26 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cafemeals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafemeals',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafes', to='products.Product'),
        ),
    ]
