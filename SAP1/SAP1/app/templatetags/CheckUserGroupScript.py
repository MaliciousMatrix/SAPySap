from django.contrib.auth.models import User, Group;
from django import template

register = template.Library()

@register.filter(name='ManagerCheck')
def CheckManagerGroup(user):
    return True if user.groups.filter(name='Manager').exists() else False

@register.filter(name='EmployeeCheck')
def CheckEmployeeGroup(user):
    return True if user.groups.filter(name='Employee').exists() else False

@register.filter(name='ScheduleCheck')
def CheckScheduler(user):
    return True if user.groups.filter(name='Shift Supervisor').exists() else False