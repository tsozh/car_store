# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0014_order_uaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='carprice',
            field=models.FloatField(null=True, verbose_name='车价格'),
        ),
    ]
