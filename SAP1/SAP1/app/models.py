"""
Definition of models.
"""

from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return_string = self.user.first_name + ' ' + self.user.last_name + '\'s profile'
        return return_string

    GENDER_CHOICES = (
		('M', 'Male'),
		('F','Female'),
		)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    pay_grade = models.FloatField()
    minimum_hours_per_week = models.IntegerField()
    target_hours_per_week = models.IntegerField()
    maximum_hours_per_week = models.IntegerField()
    maximum_hours_per_day = models.IntegerField()

    def get_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_days_off(self):
        #roles = list(filter(lambda x: self in x.tasks.all(), Role.objects.all()))
        #tasks = list(filter(lambda x: x.template.id == self.id, Task.objects.all()))
        days_off = list(filter(lambda x: x.user.id == self.id, TimeOffRequest.objects.all()))
        return days_off

    def get_availabilities(self):
        availability = Availability.objects.filter(profile_id = self.id).values()
        return availability

    def get_preferences(self):
        preferences = list(filter(lambda x: x.user.id == self.id, Preference.objects.all()))
        return preferences

    def get_group(self):
        return_string = "";
        for x in self.user.groups.all():
            return_string+= str(x) + ", ";
        return return_string;

    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.user.email
    def get_pay_grade(self):
        return self.pay_grade

   
@receiver(post_save, sender=Profile, dispatch_uid='profile_notification')
def profile_update_notifications(sender, instance, **kwargs):
    notification = Notification()
    
    notification.time_sent = datetime.now()
    notification.user = instance.user
    notification.title = 'Your profile has been changed'
    notification.message = ''
       
    is_disconnected = post_save.disconnect(profile_update_notifications, sender=Profile, dispatch_uid='profile_notification')
    if is_disconnected:
        notification.save()
    is_reconnected = post_save.connect(profile_update_notifications, sender=Profile, dispatch_uid='profile_notification')

class Vehicle(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    make = models.CharField(max_length=30, blank=True)
    model = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=30, blank=True)
    plate = models.CharField(max_length=8, blank=True)
    year = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.profile.user.first_name + "\'s " + self.year + " " + self.make + " " + self.model
 
class OptimizationSettings(models.Model):
    avoid_overtime = models.BooleanField()
    start_overtime_at = models.IntegerField()
    take_preferernces_into_account = models.BooleanField()
    allow_split_shifts = models.BooleanField()

class Availability(models.Model):

    DAY_CHOICES = (
		(0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
		(6, 'Saturday'),
        )
    day = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField(blank=True, default="6:00")
    end_time = models.TimeField(blank=True, default="22:00")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    def get_day_as_string(self):
        return self.DAY_CHOICES[self.day][1]

    def __str__(self):
        d = self.DAY_CHOICES[self.day][1]
        return str(self.start_time) + " - " + str(self.end_time);
    def get_id(self):
        return self.profile.id;
    def get_day(self):
        return self.day;
    def get_time(self):
        return str(self.start_time) + " - " + str(self.end_time);

class TimeOffRequest(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    day = models.DateField()
    STATE_CHOICES = (
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Denied'),
    )
    state = models.IntegerField(choices=STATE_CHOICES, default=0)
    reason_requested = models.CharField(max_length = 200)
    reason_denied = models.CharField(max_length = 200)

    def get_is_approved(self):
        return self.state == 1;

    def __str__(self):
        user_name = self.user.user.first_name
        separator = '-'
        current_state = str(self.STATE_CHOICES[state][1])
        return user_name + separator + str(day) + separator + current_state


class Certification(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length = 30)
    settings = models.ForeignKey(OptimizationSettings, on_delete=models.CASCADE, default = 1)
    def __str__(self):
        return self.name


    def get_roles(self):
        tasks = self.get_tasks()
        roles = []
        for t in tasks:
            for role in t.get_roles():
                if role not in roles:
                    roles.append(role)
        return roles

    def get_tasks(self):
        tasks = Task.objects.filter(template_id = self.id).values()
        return tasks;

class Schedule(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def get_tasks(self):
        tasks = AssignedTask.objects.filter(schedule_id = self.id).values()
        return tasks;

class Location(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Task(models.Model):

    DAY_CHOICES = (
		(0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
		(6, 'Saturday'),
        )

    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    task_name = models.CharField(max_length = 20)
    task_description = models.CharField(max_length = 140, default = 'Task Description')
    required_number_of_employees = models.IntegerField()

    start_day = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()

    end_day = models.IntegerField(choices=DAY_CHOICES)
    end_time = models.TimeField()

    required_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)

    def get_start_day_string(self):
        return self.__get_day_as_string(self.start_day)

    def get_end_day_string(self):
        return self.__get_day_as_string(self.end_day)

    def __get_day_as_string(self, day):
        return self.DAY_CHOICES[day][1]

    def __str__(self):
        template_name = self.template.name
        start_d = self.DAY_CHOICES[self.start_day][1]
        end_d = self.DAY_CHOICES[self.end_day][1]
        days_are_same = start_d == end_d

        if days_are_same:
            timespan = start_d + ' ' + str(self.start_time) + ' - ' + str(self.end_time)
        else:
            timespan = start_d + ' ' + str(self.start_time) + ' - ' + str(end_d) + ' ' + str(self.end_time)

        return_string = template_name + '\'s task ' + self.task_name + ' (' + timespan + ') '

        if self.location is not None:
            return_string += '@ ' + self.location.name + ' '

        return_string += ' [' + str(self.required_number_of_employees) + ' ' + self.required_group.name

        if self.required_number_of_employees > 1:
            return_string += 's'

        return_string += ']'

        return return_string

    def get_roles(self):
        roles = list(filter(lambda x: self in x.tasks.all(), Role.objects.all()))
        return str(roles)
    
    def get_time(self):
        start_d = self.DAY_CHOICES[self.start_day][1]
        end_d = self.DAY_CHOICES[self.end_day][1]
        days_are_same = start_d == end_d

        if days_are_same:
            timespan = str(self.start_time) + ' - ' + str(self.end_time)
        else:
            timespan = start_d + ' ' + str(self.start_time) + ' - ' + str(end_d) + ' ' + str(self.end_time)
        return timespan

    def get_name(self):
        return str(self.task_name)

    def get_location(self):
          if self.location is None:
            returnString ="No Location Specified"
            return returnString
          else:
            returnString = str(self.location)
            return returnString

    def get_employees(self):
        returnString = str(self.required_number_of_employees)
        return returnString

    def get_days(self):
        returnString = self.DAY_CHOICES[self.start_day][1]
        return returnString



    

class Role(models.Model):
    name = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Task)
    number_of_employees_needed = models.IntegerField()

    def __str__(self):
        return self.name

class AssignedRole(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    force_assigned = models.BooleanField(default=False)

class AssignedTask(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    role = models.ForeignKey(AssignedRole, on_delete=models.CASCADE, blank=True, null=True)
    force_assigned = models.BooleanField(default=False)

@receiver(post_save, sender=AssignedTask, dispatch_uid='schedule_notification')
def schedule_update_notifications(sender, instance, **kwargs):
    notification = Notification()
    
    notification.time_sent = datetime.now()
    notification.user = instance.user
    notification.title = 'Your Work Schedules have been Updated'
    notification.message = 'Schedule: ' + str(instance.schedule.name) + \
        '     Task assigned: ' + str(instance.task.task_name) + \
        '     Day scheduled: ' + str(instance.date)
       
    is_disconnected = post_save.disconnect(schedule_update_notifications, sender=AssignedTask, dispatch_uid='schedule_notification')
    if is_disconnected:
        notification.save()
    is_reconnected = post_save.connect(schedule_update_notifications, sender=AssignedTask, dispatch_uid='schedule_notification')


class DayOff(models.Model):
    DAY_CHOICES = (
		(0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
		(6, 'Saturday'),
        )

    day = models.IntegerField(choices=DAY_CHOICES)

class Preference(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)

    PREFERENCE_CHOICES = (
        (0, 'Cannot Work'),
        (1, 'Strongly Dislike'),
        (2, 'Dislike'),
        (3, 'Neutral'),
        (4, 'Like'),
        (5, 'Strongly Like')
        )

    like = models.IntegerField(choices=PREFERENCE_CHOICES)
    reason = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        username = self.user.user.first_name
        cat = self.category.name
        pref = self.PREFERENCE_CHOICES[self.like][1]
        return username + ' ' + cat + ' ' + pref

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255, default = 'Notification Title')
    message = models.TextField(default = 'Notification Message', blank = True)
    time_sent = models.DateTimeField(default = datetime.now())
    is_selected = models.BooleanField(default = False)

    def __str__(self):
        return self.title + ' for ' + self.user.first_name + ' ' + self.user.last_name