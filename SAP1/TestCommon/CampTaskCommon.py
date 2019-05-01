import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration')
from availability import Availability
from category import Category
from duration import Duration
from group import Group
from location import Location 
from preference import Preference
from role import Role
from staff_member import StaffMember
from task import Task
from TestCommon import CommonTestFunctions

class CampTaskCommon():
    def get(self, group, location, category, name, duration, num_employees):
        self.id = self.id +1
        return Task(self.id, name, duration, num_employees, group, location, category)

    generic = CommonTestFunctions()
    id = 1000
    def _afternoon_times(self):
        return [
            self.generic.camp_duration(14, 15, 2, 0, 30),
            self.generic.camp_duration(14, 15, 3, 0, 30),
            self.generic.camp_duration(14, 15, 4, 30, 30),
            self.generic.camp_duration(14, 15, 5, 0, 30),
            self.generic.camp_duration(14, 15, 6, 0, 30),

            self.generic.camp_duration(16, 17, 2, 0, 30),
            self.generic.camp_duration(16, 17, 3, 0, 30),
            self.generic.camp_duration(16, 17, 4, 0, 30),
            self.generic.camp_duration(16, 17, 5, 0, 30)
        ]

    def getAfternoon(self, group, location, category, name, num_employees):
        l = []
        for time in self._afternoon_times():
            l.append(self.get(group, location, category, name, time, num_employees))
        return l


#def task(self, group, location, category, duration, id=15, name='Test Task', required_number_of_employees=1):
#        return Task(id, name, duration, required_number_of_employees, group, location, category)
