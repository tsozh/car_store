# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_auto_20180207_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.User', verbose_name='用户'),
        ),
    ]
