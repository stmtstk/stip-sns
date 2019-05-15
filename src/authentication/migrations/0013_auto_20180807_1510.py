# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-07 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='scan_csv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='scan_pdf',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='scan_post',
            field=models.BooleanField(default=True),
        ),
    ]
