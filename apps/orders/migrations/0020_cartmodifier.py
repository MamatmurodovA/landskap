# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-21 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20181213_1647'),
        ('orders', '0019_auto_20181206_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_modifier', to='orders.Cart')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_modifier_items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_modifier', to='products.Product')),
            ],
            options={
                'verbose_name': 'Cart modifier item',
                'verbose_name_plural': 'Cart modifier items',
            },
        ),
    ]
