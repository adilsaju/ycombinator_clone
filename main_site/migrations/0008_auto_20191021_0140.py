# Generated by Django 2.2.6 on 2019-10-20 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_auto_20191020_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
