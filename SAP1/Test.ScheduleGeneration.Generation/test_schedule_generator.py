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
from ScheduleGenerator import ScheduleGenerator

class TestScheduleGenerator(unittest.TestCase):

    def test_get_unassigned_tasks(self):
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

        generator = ScheduleGenerator(staff_members, [], tasks)
        self.assertTrue(generator.has_unassigned_tasks())
        self.assertEqual(generator.get_amount_of_unassigned_tasks(), len(tasks) - 0)
        self.assertEqual(len(generator.get_unassigned_tasks()), len(tasks) - 0)
        self.assertTrue(task1 in generator.get_unassigned_tasks())
        self.assertTrue(task2 in generator.get_unassigned_tasks())

        # Assign member1 the first task. 
        member1.assign_task(task1)

        self.assertTrue(generator.has_unassigned_tasks())
        self.assertEqual(generator.get_amount_of_unassigned_tasks(), len(tasks) - 1)
        self.assertEqual(len(generator.get_unassigned_tasks()), len(tasks) - 1)
        self.assertFalse(task1 in generator.get_unassigned_tasks())
        self.assertTrue(task2 in generator.get_unassigned_tasks())

        # assign the other task.
        member2.assign_task(task2)

        self.assertFalse(generator.has_unassigned_tasks())
        self.assertEqual(generator.get_amount_of_unassigned_tasks(), len(tasks) - 2)
        self.assertEqual(len(generator.get_unassigned_tasks()), len(tasks) - 2)
        self.assertFalse(task1 in generator.get_unassigned_tasks())
        self.assertFalse(task2 in generator.get_unassigned_tasks())

if __name__ == '__main__':
    unittest.main()