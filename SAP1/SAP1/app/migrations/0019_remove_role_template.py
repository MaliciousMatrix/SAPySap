# Generated by Django 2.1.3 on 2019-04-02 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_role_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='template',
        ),
    ]
