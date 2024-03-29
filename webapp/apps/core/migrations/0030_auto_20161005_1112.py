# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 11:12
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('external_api', '0004_vendor'),
        ('core', '0029_fundorderitem_sip_reminder_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to='external_api.Vendor'),
        ),
    ]
