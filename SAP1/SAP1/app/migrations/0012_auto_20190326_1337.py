# Generated by Django 2.1.3 on 2019-03-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190321_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='maximum_hours_per_week',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='minimum_hours_per_week',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
