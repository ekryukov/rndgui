# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prd', '0004_auto_20170519_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='date_released',
            field=models.DateField(null=True, verbose_name='Build date'),
        ),
        migrations.AlterField(
            model_name='release',
            name='date_released',
            field=models.DateField(null=True, verbose_name='Release date'),
        ),
    ]