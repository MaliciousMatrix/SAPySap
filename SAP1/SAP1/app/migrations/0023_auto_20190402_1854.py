# Generated by Django 2.1.3 on 2019-04-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_profile_max_hours_per_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='reason',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
