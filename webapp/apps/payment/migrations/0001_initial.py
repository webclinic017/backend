# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 11:06
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('source_id', models.CharField(default='NA', max_length=15, verbose_name='Source Id')),
                ('biller_id', models.CharField(default='NA', max_length=20, verbose_name='Biller Id')),
                ('txn_amount', models.FloatField(max_length=8, verbose_name='Transaction Amount')),
                ('txt_bank_id', models.CharField(max_length=3, verbose_name='Bank Name')),
                ('additional_info_1', models.CharField(max_length=100, unique=True, verbose_name='Order Number')),
                ('additional_info_2', models.CharField(default='NA', max_length=100, verbose_name='Folio Number')),
                ('additional_info_3', models.CharField(default='NA', max_length=100, verbose_name='User Login Id/CRN')),
                ('additional_info_4', models.CharField(default='ARN-108537', max_length=100, verbose_name='Distributer Id')),
                ('additional_info_5', models.CharField(default='BSE-NA', max_length=100, verbose_name='AMC Id ')),
                ('additional_info_6', models.CharField(default='NONLIQUID', max_length=100, verbose_name='Fund Type')),
                ('additional_info_7', models.CharField(default='RESIDENT', max_length=100, verbose_name='Investor Type/Tax Status')),
                ('additional_info_8', models.DateTimeField(auto_now_add=True, max_length=100, verbose_name='Transaction Time')),
                ('additional_info_9', models.CharField(default='BSE', max_length=100, verbose_name='Scheme Code')),
                ('additional_info_10', models.CharField(default='NA', max_length=100, verbose_name='Sender SIP Registration No.')),
                ('additional_info_11', models.CharField(default='L', max_length=100, verbose_name='Transaction Type')),
                ('additional_info_12', models.CharField(default='NA', max_length=100, verbose_name='AMC Code')),
                ('txt_merchant_user_ref_no', models.CharField(blank=True, default=None, max_length=17, null=True, verbose_name='Bank Account Number')),
                ('txn_reference_no', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Transaction Reference Number')),
                ('txn_status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Success'), (2, 'Failure')], default=0)),
                ('auth_status', models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='AuthStatus')),
                ('merchant_id', models.CharField(blank=True, default='FINASKUS', max_length=100, null=True, verbose_name='Merchant Id')),
                ('customer_id', models.CharField(max_length=100, unique=True, verbose_name='Customer Id')),
                ('product_id', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Product Id')),
                ('response_string', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('request_string', django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
