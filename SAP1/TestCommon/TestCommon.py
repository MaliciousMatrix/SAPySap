import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Generetion')
from availability import Availability
from category import Category
from duration import Duration
from group import Group
from location import Location 
from preference import Preference
from role import Role
from staff_member import StaffMember
from task import Task
from scheduler_settings import SchedulerSettings

class CommonTestFunctions():

    def staff_member(self, id=5, name='Ted Mosby', min_hpw=5, target_hpw=40, max_hpw=50, max_hpd=10, availability=[], preferences=[], groups=[]):
        return StaffMember(id, name, min_hpw, target_hpw, max_hpw, max_hpd, availability, preferences, groups)

    def astaff_member(self, name, min_hpw, target_hpw, max_hpw, max_hpd, availability, preferences, groups):
        id = self._get_next_staff_member_id()
        s = self.staff_member(id, name, min_hpw, target_hpw, max_hpw, max_hpd, availability, preferences, groups)
        self.created_staff_members.append(s)
        return s

    def availability(self, start_hour=6, end_hour=22, start_day=1, end_day=1):
        return Availability(self.duration(start_hour, end_hour, 0, 0, start_day, end_day))

    def camp_availability(self, day, start_hour, end_hour, start_minute=0, end_minute=0):
        start_a = datetime.datetime(2018, 7, day, start_hour, start_minute, 0)
        end_a = datetime.datetime(2018, 7, day, end_hour, end_minute, 0)
        return Availability(Duration(start_a, end_a))

    def category(self, id=2, name='Test Category'):
        return Category(id, name)

    def group(self, id=6, name='Test Group'):
        return Group(id, name)

    def duration(self, start_hour=10, end_hour=15, start_minute=0, end_minute=0, start_day=1, end_day=1):
        start_a = datetime.datetime(2000, 1, start_day, start_hour, start_minute, 0)
        end_a = datetime.datetime(2000, 1, end_day, end_hour, end_minute, 0)
        return Duration(start_a, end_a)

    def camp_duration(self, start_hour, end_hour, day, start_minute=0, end_minute=0):
        start_a = datetime.datetime(2018, 7, day, start_hour, start_minute, 0)
        end_a = datetime.datetime(2018, 7, day, end_hour, end_minute, 0)
        return Duration(start_a, end_a)

    def preference(self, category, likeness=0, can_work=True):
        return Preference(category, likeness, can_work)

    def location(self, id=10, name='Test Location'):
        return Location(id, name)

    def task(self, group, location, category, duration, id=15, name='Test Task', required_number_of_employees=1):
        return Task(id, name, duration, required_number_of_employees, group, location, category)

    def atask(self, group, location, category, duration, name, req_emp_num=1):
        id = self._get_next_task_id()
        t = self.task(group, location, category, duration, id, name, req_emp_num)
        self.created_tasks.append(t)
        return t

    def settings(self, overtime_start_at=40, use_preferences=True, avoid_overtime=True):
        return SchedulerSettings(avoid_overtime, overtime_start_at, use_preferences)

    def role(self, tasks, required_number_of_employees=1, name='Role', id=None):
        if id == None:
            id = self._get_next_role_id()

        r = Role(id, name, tasks, required_number_of_employees)
        self.created_roles.append(r)
        return r

    def _get_next_role_id(self):
        self._role_id = self._role_id + 1
        return self._role_id

    def _get_next_task_id(self):
        self._task_id = self._task_id + 1
        return self._task_id

    def _get_next_staff_member_id(self):
        self._staff_member_id = self._staff_member_id + 1
        return self._staff_member_id

    _role_id = 0
    _task_id = 0
    _staff_member_id = 0

    created_tasks = []
    created_roles = []
    created_staff_members = []


    #endregion 
