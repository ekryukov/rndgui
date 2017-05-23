# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prd', '0005_auto_20170519_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='date_released',
            field=models.DateField(blank=True, null=True, verbose_name='Build date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wiki_url',
            field=models.URLField(blank=True, null=True, verbose_name='Wiki/Confluence URL'),
        ),
        migrations.AlterField(
            model_name='release',
            name='date_released',
            field=models.DateField(blank=True, null=True, verbose_name='Release date'),
        ),
    ]
