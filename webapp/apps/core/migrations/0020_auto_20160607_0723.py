# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 07:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0019_remove_fund_fund_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupedRedeemDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('redeem_status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Ongoing'), (2, 'Complete'), (3, 'Cancelled')], default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='redeemdetail',
            name='fund',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Fund'),
        ),
        migrations.AddField(
            model_name='redeemdetail',
            name='is_cancelled',
            field=models.BooleanField(default=False, verbose_name='is cancelled'),
        ),
        migrations.AddField(
            model_name='redeemdetail',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='is verified'),
        ),
        migrations.AddField(
            model_name='redeemdetail',
            name='redeem_amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='redeemdetail',
            name='redeem_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='redeemdetail',
            name='unit_redeemed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='groupedredeemdetail',
            name='redeem_details',
            field=models.ManyToManyField(to='core.RedeemDetail'),
        ),
        migrations.AddField(
            model_name='groupedredeemdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
