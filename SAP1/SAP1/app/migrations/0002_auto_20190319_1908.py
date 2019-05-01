# Generated by Django 2.1.3 on 2019-03-20 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskName', models.CharField(max_length=20)),
                ('EmpNum', models.IntegerField()),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TimeOffRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('state', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Denied')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='timeoffrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AddField(
            model_name='task',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Template'),
        ),
        #migrations.AddField(
        #    model_name='assignedtask',
        #    name='schedule',
        #    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Schedule'),
        #),
        migrations.AddField(
            model_name='assignedtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Task'),
        ),
        migrations.AddField(
            model_name='assignedtask',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]