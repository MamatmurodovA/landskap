# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 11:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0066_cashier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cafe_owner', to=settings.AUTH_USER_MODEL, verbose_name='Cafe owner'),
        ),
    ]
