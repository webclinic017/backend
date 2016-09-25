# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 05:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('external_api', '0004_vendor'),
        ('profiles', '0015_auto_20160928_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('ucc', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('mandate_registered', models.BooleanField(default=False)),
                ('mandate_reg_no', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Mandate Registration Number')),
                ('ucc_registered', models.BooleanField(default=False)),
                ('fatca_filed', models.BooleanField(default=False)),
                ('tiff_mailed', models.BooleanField(default=False)),
                ('tiff_accepted', models.BooleanField(default=False)),
                ('mandate_status', models.CharField(blank=True, choices=[('0', 'Pending'), ('1', 'Ongoing'), ('2', 'Completed')], default='0', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='uservendor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='uservendor',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_vendor', to='external_api.Vendor'),
        ),
        migrations.AlterUniqueTogether(
            name='uservendor',
            unique_together=set([('user', 'vendor')]),
        ),
    ]