# Generated by Django 2.1.3 on 2019-04-07 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_role_number_of_employees_needed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='max_hours_per_day',
            new_name='maximum_hours_per_day',
        ),
    ]
