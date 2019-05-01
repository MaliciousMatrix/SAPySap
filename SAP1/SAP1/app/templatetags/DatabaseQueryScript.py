from app.models import Profile, Availability, Template, Schedule, Task, AssignedTask
from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.conf import settings

from django.contrib.auth.models import User, Group;
from django import template

register = template.Library()

@register.filter(name='SaveTasks')
def SaveTasksToTempDatabase(task, schedule):
    class SavedTasks(models.Model):
        task = models.ForeignKey(Task, on_delete=CASCADE)
        scheduleID = models.ForeignKey(Schedule, on_delete=CASCADE)

    for x in task:
        t = SavedTasks(x.id, schedule.id)
        t.save()


@register.filter(name='SaveEmployees')
def SaveEmployeesToTempDatabase(employee, schedule):
    class SavedEmployee(models.Model):
        employee = models.ForeignKey(Profile, on_delete=CASCADE)
        scheduleID = models.ForeignKey(Schedule, on_delete=CASCADE)
    for x in employee:
        e = SavedEmployee(x.id, schedule.id)
        e.save()

@register.filter(name='PullEmployees')
def PullEmployeesFromDatabase():
    AllEmployees = Profile.objects.all()
    return AllEmployees

@register.filter(name='PullTemplate')
def PullTemplateFromDataBase():
    AllTemplate = Template.objects.all()
    return AllTemplate

@register.filter(name='PullTasks')
def PullTasksFromDatabase():
    AllTasks = Task.objects.all()
    return AllTasks

@register.filter(name='PullSavedEmployees')
def PullSavedEmployeesFromDatabase():
    SavedEmployees = SavedEmployee.objects.all()
    return SavedEmployees

@register.filter(name='PullSavedTasks')
def PullSavedTasksFromDatabase():
    Saved = SavedTasks.objects.all()
    return Saved
