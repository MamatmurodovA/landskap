# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20180927_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripetransaction',
            name='card_id',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='stripetransaction',
            name='customer_id',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='stripetransaction',
            name='token',
            field=models.CharField(max_length=254, null=True),
        ),
    ]