# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-14 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0010_auto_20170802_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='sharing_group',
            field=models.CharField(choices=[(b'chemical', 'SHARING_GROUP_Chemical'), (b'commercial', 'SHARING_GROUP_Commercial Facilities'), (b'communication', 'SHARING_GROUP_Communications'), (b'critical', 'SHARING_GROUP_Critical Manufacturing'), (b'dams', 'SHARING_GROUP_Dams'), (b'defense', 'SHARING_GROUP_Defense Industrial Base'), (b'emergency', 'SHARING_GROUP_Emergency Services'), (b'energy', 'SHARING_GROUP_Energy'), (b'financial', 'SHARING_GROUP_Financial Services'), (b'food', 'SHARING_GROUP_Food and Agriculture'), (b'government', 'SHARING_GROUP_Government Facilities'), (b'healthcare', 'SHARING_GROUP_Healthcare and Public Health'), (b'information', 'SHARING_GROUP_Information Technology'), (b'nuclear', 'SHARING_GROUP_Nuclear Reactors, Materials, and Waste'), (b'transport', 'SHARING_GROUP_Transportation Systems'), (b'water', 'SHARING_GROUP_Water and Wastewater Systems')], default=b'csc', max_length=128, null=True),
        ),
    ]
