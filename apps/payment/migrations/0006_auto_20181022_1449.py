# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_paypaltransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypaltransaction',
            name='transaction_id',
            field=models.TextField(editable=False),
        ),
    ]
