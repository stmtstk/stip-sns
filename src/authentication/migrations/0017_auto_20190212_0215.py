# Generated by Django 1.10.4 on 2019-02-12 08:15


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0022_auto_20190212_0215'),
        ('groups', '0002_auto_20190212_0215'),
        ('authentication', '0016_profile_indicator_white_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='region',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
