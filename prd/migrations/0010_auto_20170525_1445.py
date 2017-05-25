# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prd', '0009_remove_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleasePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Module name')),
                ('gitlab_id', models.IntegerField(blank=True, choices=[(558, 'forabank.SVWeb'), (548, 'RnD GUI'), (540, 'bisa.svng.web'), (530, 'IgniteSupport'), (529, 'svfe-sbrf-scripts'), (528, 'svlb-sbrf'), (527, 'belgaz-integration-gateway'), (526, 'hsm-client'), (521, 'rb.server.integration_avers'), (520, 'group-b-web-interface'), (519, 'ecom-reg'), (518, 'com.bpcbt.finstream'), (517, 'Autotest carousel'), (515, 'com.bpcbt.fraud.tests'), (514, 'auth'), (513, 'ru.bpc.orach'), (506, 'DevOps REST API'), (505, 'Voila'), (502, 'watchdog-listener'), (499, 'InterCard.iso20022ws')], null=True, verbose_name='Gitlab project')),
                ('one_module', models.BooleanField(default=True, help_text='Product have only one module(Product=Module)', verbose_name='One module')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='specification_repo',
            field=models.IntegerField(blank=True, choices=[(558, 'forabank.SVWeb'), (548, 'RnD GUI'), (540, 'bisa.svng.web'), (530, 'IgniteSupport'), (529, 'svfe-sbrf-scripts'), (528, 'svlb-sbrf'), (527, 'belgaz-integration-gateway'), (526, 'hsm-client'), (521, 'rb.server.integration_avers'), (520, 'group-b-web-interface'), (519, 'ecom-reg'), (518, 'com.bpcbt.finstream'), (517, 'Autotest carousel'), (515, 'com.bpcbt.fraud.tests'), (514, 'auth'), (513, 'ru.bpc.orach'), (506, 'DevOps REST API'), (505, 'Voila'), (502, 'watchdog-listener'), (499, 'InterCard.iso20022ws')], help_text='Gitlab repostitory ID for product specifications', null=True, verbose_name='Specifications repository'),
        ),
        migrations.AlterField(
            model_name='product',
            name='inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acm.Institution', verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='releasepart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prd.Product'),
        ),
        migrations.AddField(
            model_name='releasepart',
            name='release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prd.Release'),
        ),
    ]