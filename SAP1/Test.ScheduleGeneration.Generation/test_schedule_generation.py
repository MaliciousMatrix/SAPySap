import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Generation')

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

class TestScheduleGeneration(unittest.TestCase):

    def test_one_task_one_user_assign(self):
        start_a = datetime.datetime(2000, 1, 1, 6, 0, 0)
        end_a = datetime.datetime(2000, 1, 1, 22, 0, 0)
        availability = [Availability(Duration(start_a, end_a))]
        category = Category(1, 'TestCategory')
        preferences = [Preference(category, 0, True)]
        groups = [Group(1, 'Employee')]
        generic = CommonTestFunctions()

        staff_member = StaffMember(1, 'TestMember', 0, 40, 80, 10, availability, preferences, groups)

        start_t = datetime.datetime(2000, 1, 1, 9, 0, 0)
        end_t = datetime.datetime(2000, 1, 1, 16, 0, 0)
        task_time = Duration(start_t, end_t)
        location = Location(1, 'TestLocation')
        task = Task(1, 'TestTask', task_time, 1, groups[0], location, category)

        staff_members = [staff_member]
        roles = []
        tasks = [task]
        settings = generic.settings(40, True)
        generator = ScheduleGenerator(staff_members, roles, tasks)
        generator.schedule(settings) 
        self.assertTrue(staff_member.has_task(task))

        self.assertFalse(generator.has_unassigned_tasks())

    def test_one_task_with_multiple_employees_gets_assigned(self):
        generic = CommonTestFunctions()
        location = generic.location()
        category = generic.category()
        group = generic.group()
        duration = generic.duration(6, 14)
        task1 = generic.task(group, location, category, duration, required_number_of_employees=2)

        availabilities = [generic.availability(6, 22)]
        groups = [group]
        member1 = generic.staff_member(1, availability = availabilities, groups = groups)
        member2 = generic.staff_member(2, availability = availabilities, groups = groups)

        tasks = [task1]
        staff_members = [
            member1,
            member2,
            ]

        roles = []
        settings = generic.settings(40, True)
        generator = ScheduleGenerator(staff_members, roles, tasks)
        generator.schedule(settings) 
        self.assertTrue(member1.has_task(task1))
        self.assertTrue(member2.has_task(task1))

        self.assertFalse(generator.has_unassigned_tasks())

    def test_employees_with_different_availability_get_different_tasks(self):
        generic = CommonTestFunctions()
        location = generic.location()
        category = generic.category()
        group = generic.group()

        duration1 = generic.duration(6, 14)
        task1 = generic.task(group, location, category, duration1)

        duration2 = generic.duration(10, 18)
        task2 = generic.task(group, location, category, duration2)

        duration3 = generic.duration(14, 22)
        task3 = generic.task(group, location, category, duration3)

        groups = [group]

        availabilities1 = [generic.availability(6, 14)]
        member1 = generic.staff_member(1, availability = availabilities1, groups = groups)

        availabilities2 = [generic.availability(10, 18)]
        member2 = generic.staff_member(2, availability = availabilities2, groups = groups)

        availabilities3 = [generic.availability(14, 22)]
        member3 = generic.staff_member(3, availability = availabilities3, groups = groups)

        tasks = [
            task1,
            task2,
            task3,
            ]

        staff_members = [
            member1,
            member2,
            member3,
            ]

        roles = []

        settings = generic.settings(40, True)
        generator = ScheduleGenerator(staff_members, roles, tasks)
        generator.schedule(settings) 

        self.assertTrue(member1.has_task(task1))
        self.assertTrue(member2.has_task(task2))
        self.assertTrue(member3.has_task(task3))

        self.assertFalse(generator.has_unassigned_tasks())

    def test_employees_of_different_groups_get_different_tasks(self):
        generic = CommonTestFunctions()
        location = generic.location()
        category = generic.category()

        group1 = generic.group(1, 'One')
        group2 = generic.group(2, 'Two')

        duration = generic.duration(6, 14)
        task1 = generic.task(group1, location, category, duration)
        task2 = generic.task(group2, location, category, duration)
        
        availabilities = [generic.availability(6, 14)]

        groups1 = [group1]
        groups2 = [group2]

        member1 = generic.staff_member(1, availability = availabilities, groups = groups1)
        member2 = generic.staff_member(2, availability = availabilities, groups = groups2)

        tasks = [
            task1,
            task2,
            ]

        staff_members = [
            member1,
            member2,
            ]

        roles = []

        settings = generic.settings(40, True)
        generator = ScheduleGenerator(staff_members, roles, tasks)
        generator.schedule(settings) 

        self.assertTrue(member1.has_task(task1))
        self.assertFalse(member1.has_task(task2))
        self.assertTrue(member2.has_task(task2))
        self.assertFalse(member2.has_task(task1))

        self.assertFalse(generator.has_unassigned_tasks())

    def test_employee_who_cant_work_doesnt_get_task(self):
        generic = CommonTestFunctions()
        location = generic.location()

        category1 = generic.category(1, 'Cat One')
        category2 = generic.category(2, 'Cat Two')

        group = generic.group(1, 'Group One')

        duration = generic.duration(6, 14)
        task1 = generic.task(group, location, category1, duration)
        task2 = generic.task(group, location, category2, duration)
        
        availabilities = [generic.availability(6, 14)]
        preference = generic.preference(category1, can_work=False)

        preferences = [preference]
        groups = [group]

        member1 = generic.staff_member(1, availability = availabilities, groups = groups, preferences= preferences)
        member2 = generic.staff_member(2, availability = availabilities, groups = groups)

        tasks = [
            task1,
            task2,
            ]

        staff_members = [
            member1,
            member2,
            ]

        roles = []
        generator = ScheduleGenerator(staff_members, roles, tasks)
        settings = generic.settings()
        generator.schedule(settings) 

        self.assertFalse(member1.has_task(task1))
        self.assertTrue(member1.has_task(task2))

        self.assertTrue(member2.has_task(task1))
        self.assertFalse(member2.has_task(task2))

        self.assertFalse(generator.has_unassigned_tasks())





if __name__ == '__main__':
    unittest.main()