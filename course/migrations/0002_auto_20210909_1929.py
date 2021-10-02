# Generated by Django 3.2.6 on 2021-09-09 13:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='shop\\images'),
        ),
        migrations.AddField(
            model_name='course',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 9, 13, 59, 8, 780215, tzinfo=utc)),
        ),
    ]