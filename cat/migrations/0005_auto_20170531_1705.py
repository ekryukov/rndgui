# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0004_remove_dbinstance_dbname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbinstance',
            name='sid',
            field=models.CharField(blank=True, default='SV', max_length=20, null=True, verbose_name='SID'),
        ),
        migrations.AlterField(
            model_name='dbinstance',
            name='weight',
            field=models.IntegerField(choices=[('Big', 'For SmartVista project'), ('Medium', 'For SMSGate, SSO projects'), ('Small', 'For other project')], verbose_name='Weight'),
        ),
    ]
