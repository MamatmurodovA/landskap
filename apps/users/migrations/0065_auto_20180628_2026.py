# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 15:26
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geosimple.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0064_auto_20180628_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe_name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('address', models.TextField(blank=True, null=True)),
                ('call_center', models.CharField(max_length=13)),
                ('website', models.URLField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Blocked'), (1, 'Active'), (2, 'Pending')], default=0)),
                ('location', geosimple.fields.GeohashField(db_index=True, default={'latitude': 50.822482, 'longitude': -0.141449}, editable=False, max_length=12)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_category', to='users.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='company',
            name='category',
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.RemoveField(
            model_name='useravatars',
            name='user',
        ),
        migrations.RemoveField(
            model_name='album',
            name='company',
        ),
        migrations.RemoveField(
            model_name='bookmarks',
            name='company',
        ),
        migrations.RemoveField(
            model_name='recentlyviewed',
            name='company',
        ),
        migrations.RemoveField(
            model_name='review',
            name='company',
        ),
        migrations.RemoveField(
            model_name='weektime',
            name='company',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='date of birthday'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Cafe owner'), (2, 'Simple user')], default=2),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='UserAvatars',
        ),
        migrations.AddField(
            model_name='cafe',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='cafe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Cafe'),
        ),
        migrations.AddField(
            model_name='bookmarks',
            name='cafe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookmarked_cafe', to='users.Cafe'),
        ),
        migrations.AddField(
            model_name='recentlyviewed',
            name='cafe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Cafe'),
        ),
        migrations.AddField(
            model_name='review',
            name='cafe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Cafe'),
        ),
        migrations.AddField(
            model_name='weektime',
            name='cafe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Cafe'),
        ),
    ]
