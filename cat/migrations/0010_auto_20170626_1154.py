# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0009_auto_20170626_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='releasecarousel',
            options={'ordering': ['used', 'sort']},
        ),
    ]
