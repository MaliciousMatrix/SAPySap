# Generated by Django 2.1.7 on 2019-04-25 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20190425_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='time_sent',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 4, 57, 38, 476003)),
        ),
    ]
