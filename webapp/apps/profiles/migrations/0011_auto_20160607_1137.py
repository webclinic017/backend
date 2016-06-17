# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-07 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20160607_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_video',
            field=models.FileField(blank=True, max_length=700, null=True, upload_to='user_video/'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_video_thumbnail',
            field=models.FileField(blank=True, max_length=700, null=True, upload_to='user_video/thumbnail/'),
        ),
    ]
