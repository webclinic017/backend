# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-22 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_redeemdetail_invested_redeem_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundredeemitem',
            name='invested_redeem_amount',
            field=models.FloatField(default=0.0),
        ),
    ]
