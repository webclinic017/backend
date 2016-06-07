# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-09 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundorderitem',
            name='is_initial',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='is_lumpsum',
            field=models.BooleanField(default=False, verbose_name='is first order'),
        ),
    ]
