# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-06 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20181120_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sub_total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tax_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
