# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-10 07:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0020_feed_refer_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='refer_url',
            new_name='referred_url',
        ),
    ]
