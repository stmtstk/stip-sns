# Generated by Django 1.10.4 on 2017-07-14 00:00


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
