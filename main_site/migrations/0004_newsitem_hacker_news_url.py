# Generated by Django 2.2.6 on 2019-10-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_auto_20191019_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='hacker_news_url',
            field=models.CharField(default='', max_length=500),
        ),
    ]