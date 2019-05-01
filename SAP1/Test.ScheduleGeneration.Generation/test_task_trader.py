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
from task_trader import TaskTrader
from bad_task_assignment_exception import BadTaskAssignmentException

class TestTaskTrader(unittest.TestCase):
    def test_trade_2_tasks(self):
        generic = CommonTestFunctions()
        location = generic.location()

        category = generic.category(1, 'Cat One')

        group = generic.group(1, 'Group One')

        duration = generic.duration(6, 14)
        task1 = generic.task(group, location, category, duration, id=1)
        task2 = generic.task(group, location, category, duration, id=2)
        
        availabilities = [generic.availability(6, 14)]
        groups = [group]

        member1 = generic.staff_member(1, availability = availabilities, groups = groups)
        member2 = generic.staff_member(2, availability = availabilities, groups = groups)

        tasks = [
            task1,
            task2,
            ]

        staff_members = [
            member1,
            member2,
            ]

        member1.assign_task(task1)
        member2.assign_task(task2)

        self.assertTrue(member1.has_task(task1))
        self.assertTrue(member2.has_task(task2))

        TaskTrader().trade_2_tasks(member1, member2, task1, task2)

        self.assertTrue(member1.has_task(task2))
        self.assertTrue(member2.has_task(task1))

        self.assertFalse(member1.has_task(task1))
        self.assertFalse(member2.has_task(task2))

    def test_trade_3_tasks(self):
        generic = CommonTestFunctions()
        location = generic.location()

        category = generic.category(1, 'Cat One')

        group = generic.group(1, 'Group One')

        duration = generic.duration(6, 14)
        task1 = generic.task(group, location, category, duration, id=1)
        task2 = generic.task(group, location, category, duration, id=2)
        task3 = generic.task(group, location, category, duration, id=3)
        
        availabilities = [generic.availability(6, 14)]
        groups = [group]

        member1 = generic.staff_member(1, availability = availabilities, groups = groups)
        member2 = generic.staff_member(2, availability = availabilities, groups = groups)
        member3 = generic.staff_member(3, availability = availabilities, groups = groups)

        member1.assign_task(task1)
        member2.assign_task(task2)
        member3.assign_task(task3)

        self.assertTrue(member1.has_task(task1))
        self.assertTrue(member2.has_task(task2))
        self.assertTrue(member3.has_task(task3))

        TaskTrader().trade_3_tasks(member1, member2, member3, task1, task2, task3)

        self.assertTrue(member1.has_task(task2))
        self.assertTrue(member2.has_task(task3))
        self.assertTrue(member3.has_task(task1))

        self.assertFalse(member1.has_task(task1))
        self.assertFalse(member2.has_task(task2))
        self.assertFalse(member3.has_task(task3))

        self.assertFalse(member1.has_task(task3))
        self.assertFalse(member2.has_task(task1))
        self.assertFalse(member3.has_task(task2))

    def test_staff_doesnt_have_task(self):
        generic = CommonTestFunctions()
        location = generic.location()

        category = generic.category(1, 'Cat One')

        group = generic.group(1, 'Group One')

        duration = generic.duration(6, 14)
        task1 = generic.task(group, location, category, duration, id=1)
        task2 = generic.task(group, location, category, duration, id=2)
        
        availabilities = [generic.availability(6, 14)]
        groups = [group]

        member1 = generic.staff_member(1, availability = availabilities, groups = groups)
        member2 = generic.staff_member(2, availability = availabilities, groups = groups)

        tasks = [
            task1,
            task2,
            ]

        staff_members = [
            member1,
            member2,
            ]

        member1.assign_task(task1)

        self.assertTrue(member1.has_task(task1))
        self.assertFalse(member2.has_task(task2))

        self.assertRaises(AssertionError, TaskTrader().trade_2_tasks, member1, member2, task1, task2)

        self.assertTrue(member1.has_task(task1))
        self.assertFalse(member1.has_task(task2))

        self.assertFalse(member2.has_task(task1))
        self.assertFalse(member2.has_task(task2))

if __name__ == '__main__':
    unittest.main()