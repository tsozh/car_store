# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0017_auto_20180207_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='carname',
            field=models.CharField(max_length=20, null=True, verbose_name='车名'),
        ),
        migrations.AddField(
            model_name='comment',
            name='createdat',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='评价时间'),
        ),
    ]
