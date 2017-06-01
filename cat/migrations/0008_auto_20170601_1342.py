# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0007_stlninstance_webinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stlninstance',
            name='host_login',
            field=models.CharField(max_length=200, verbose_name='Host login'),
        ),
        migrations.AlterField(
            model_name='webinstance',
            name='host_login',
            field=models.CharField(max_length=200, verbose_name='Host login'),
        ),
        migrations.AlterField(
            model_name='webinstance',
            name='target_server',
            field=models.CharField(max_length=200, verbose_name='Server'),
        ),
    ]
