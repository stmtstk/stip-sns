# Generated by Django 1.10.4 on 2018-07-31 01:04


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0018_attachfile_feed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='ci',
            field=models.CharField(default='', max_length=128, null=True),
        ),
    ]
