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


class CampStaffCommon():

    def get_counselor(self, name, preferences, groups):
        self.id = self.id + 1
        groups.append(self.counselor)
        if name == '':
            name = 'Ted'
        return StaffMember(self.id, name, self.min_hpw, self.target_hpw, self.max_hpw, self.max_hpd, self.availability, preferences, groups)

    generic = CommonTestFunctions()
    counselor = generic.group(302, 'Counselor')
    min_hpw = 40
    target_hpw = 80
    max_hpw = 168
    max_hpd = 24
    availability = [
        generic.camp_availability(1, 12, 23),
        generic.camp_availability(2, 6, 23),
        generic.camp_availability(3, 6, 23),
        generic.camp_availability(4, 6, 23),
        generic.camp_availability(5, 6, 23),
        generic.camp_availability(6, 6, 23),
        generic.camp_availability(7, 12, 23),

        ]
    id = 0
