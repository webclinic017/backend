# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-30 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redeemdetail',
            name='redeem_status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Ongoing'), (2, 'Complete'), (3, 'Cancelled')], default=0),
        ),
    ]
