# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20180207_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='car',
        ),
        migrations.AddField(
            model_name='order',
            name='car_id',
            field=models.IntegerField(default=0, verbose_name='车id'),
        ),
        migrations.AddField(
            model_name='order',
            name='uname',
            field=models.CharField(max_length=20, null=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='car',
            name='carname',
            field=models.CharField(max_length=20, null=True, verbose_name='车名'),
        ),
    ]
