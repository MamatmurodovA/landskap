# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Cart item',
                'verbose_name_plural': 'Cart items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order_unique_id', models.CharField(blank=True, editable=False, max_length=120, null=True, unique=True, verbose_name='Order Id')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('state', models.IntegerField(blank=True, choices=[(0, 'Available'), (1, 'Awaiting Payment'), (2, 'Payment completed'), (3, 'Cancelled'), (4, 'Delivered'), (-1, 'In process')], default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.Product'),
        ),
    ]
