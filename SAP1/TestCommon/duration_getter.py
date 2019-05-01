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
from TestCommon import CommonTestFunctions
class DurationGetter:

    def sunday(start_hour, end_hour, start_minute=0, end_minute=0):
        return DurationGetter._get(1, start_hour, end_hour, start_minute, end_minute)

    def monday(start_hour, end_hour, start_minute=0, end_minute=0):
        return DurationGetter._get(2, start_hour, end_hour, start_minute, end_minute)

    def tuesday(start_hour, end_hour, start_minute=0, end_minute=0):
        return DurationGetter._get(3, start_hour, end_hour, start_minute, end_minute)

    def wednesday(start_hour, end_hour, start_minute=0, end_minute=0):
        return DurationGetter._get(4, start_hour, end_hour, start_minute, end_minute)

    def thursday(start_hour, end_hour, start_minute=0, end_minute=0):
        return DurationGetter._get(5, start_hour, end_hour, start_minute, end_minute)

    def friday(start_hour, end_hour, start_minute=0, end_minute=0):
        return DurationGetter._get(6, start_hour, end_hour, start_minute, end_minute)

    def saturday(start_hour, end_hour, start_minute=0, end_minute=0):
        return DurationGetter._get(7, start_hour, end_hour, start_minute, end_minute)

    def _get(day, start_hour, end_hour, start_minute, end_minute):
        generic = CommonTestFunctions()
        return generic.camp_duration(start_hour, end_hour, day, start_minute, end_minute)