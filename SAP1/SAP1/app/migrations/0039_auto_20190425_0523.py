# Generated by Django 2.1.7 on 2019-04-25 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20190425_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='time_sent',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 5, 23, 11, 184041)),
        ),
    ]
