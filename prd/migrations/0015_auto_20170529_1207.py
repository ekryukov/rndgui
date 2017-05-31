# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prd', '0014_auto_20170527_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='specification_repo',
            field=models.IntegerField(blank=True, choices=[(517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (436, 'DevOps Team / Carousel'), (479, 'DevOps Team / Check'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (559, 'SMSGate / Notification Specifications'), (537, 'SVWeb / FEAdapter'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (454, 'SVWeb / com.bpcbt.iso8583')], help_text='Gitlab repostitory ID for product specifications', null=True, verbose_name='Specifications repository'),
        ),
        migrations.AlterField(
            model_name='historicalreleasepart',
            name='gitlab_id',
            field=models.IntegerField(blank=True, choices=[(517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (436, 'DevOps Team / Carousel'), (479, 'DevOps Team / Check'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (559, 'SMSGate / Notification Specifications'), (537, 'SVWeb / FEAdapter'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (454, 'SVWeb / com.bpcbt.iso8583')], null=True, verbose_name='Gitlab project'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification_repo',
            field=models.IntegerField(blank=True, choices=[(517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (436, 'DevOps Team / Carousel'), (479, 'DevOps Team / Check'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (559, 'SMSGate / Notification Specifications'), (537, 'SVWeb / FEAdapter'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (454, 'SVWeb / com.bpcbt.iso8583')], help_text='Gitlab repostitory ID for product specifications', null=True, verbose_name='Specifications repository'),
        ),
        migrations.AlterField(
            model_name='releasepart',
            name='gitlab_id',
            field=models.IntegerField(blank=True, choices=[(517, 'DevOps Team / Autotest carousel'), (470, 'DevOps Team / BackOffice SmartVista2'), (561, 'DevOps Team / Camel converters'), (436, 'DevOps Team / Carousel'), (479, 'DevOps Team / Check'), (506, 'DevOps Team / DevOps REST API'), (487, 'DevOps Team / Instances'), (489, 'DevOps Team / Release list module'), (548, 'DevOps Team / RnD GUI'), (560, 'DevOps Team / SVWeb'), (562, 'DevOps Team / adapter'), (514, 'DevOps Team / auth'), (485, 'DevOps Team / installer-builder'), (464, 'DevOps Team / installer_gui'), (559, 'SMSGate / Notification Specifications'), (537, 'SVWeb / FEAdapter'), (457, 'SVWeb / SVWF'), (456, 'SVWeb / SVWF-Bankmed'), (458, 'SVWeb / SVWF-UI'), (454, 'SVWeb / com.bpcbt.iso8583')], null=True, verbose_name='Gitlab project'),
        ),
        migrations.AlterUniqueTogether(
            name='build',
            unique_together=set([('name', 'release')]),
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('name', 'product')]),
        ),
    ]