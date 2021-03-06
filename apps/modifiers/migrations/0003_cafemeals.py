# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-06 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0124_auto_20181204_1640'),
        ('modifiers', '0002_auto_20181206_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='CafeMeals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals_modifier', to='users.Cafe')),
                ('modifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafes_modifier', to='modifiers.Modifier')),
            ],
            options={
                'verbose_name': 'Cafe modifier',
                'verbose_name_plural': 'Cafe modifiers',
            },
        ),
    ]
