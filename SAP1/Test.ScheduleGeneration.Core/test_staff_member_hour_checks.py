import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\TestCommon')
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
from bad_task_assignment_exception import BadTaskAssignmentException

class TestStaffMemberHourCheck(unittest.TestCase):

    def test_get_hours_worked_on_date(self):
         generic = CommonTestFunctions()

         category = generic.category()
         location = generic.location()
         group = generic.group()

         duration1 = generic.duration(6, 10, 0, 0, 1, 1) # 4 hours
         duration2 = generic.duration(11, 17, 0, 0, 1, 1) # 6 hours
         duration3 = generic.duration(18, 19, 0, 0, 2, 2) # 1 hour

         task1 = generic.task(group, location, category, duration1, 1)
         task2 = generic.task(group, location, category, duration2, 2)
         task3 = generic.task(group, location, category, duration3, 3)
         
         availability = [
             generic.availability(6,22, 1, 1),
             generic.availability(6,22, 2, 2),
             ]
         groups = [group]
         preferences = [generic.preference(category)]
         staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups)

         date1 = datetime.date(2000, 1, 1)
         date2 = datetime.date(2000, 1, 2)
         staff_member.assign_task(task1)
         self.assertTrue(staff_member.has_task(task1))
         self.assertEqual(staff_member.get_hours_worked_on_date(date1), 4)
         self.assertEqual(staff_member.get_total_hours_working(), 4)

         staff_member.assign_task(task2)
         self.assertTrue(staff_member.has_task(task1))
         self.assertTrue(staff_member.has_task(task2))
         self.assertEqual(staff_member.get_hours_worked_on_date(date1), 10)
         self.assertEqual(staff_member.get_total_hours_working(), 10)

         staff_member.assign_task(task3)
         self.assertTrue(staff_member.has_task(task1))
         self.assertTrue(staff_member.has_task(task2))
         self.assertTrue(staff_member.has_task(task3))

         # Unchanged because the task should be on the following day. 
         self.assertEqual(staff_member.get_hours_worked_on_date(date1), 10)
         self.assertEqual(staff_member.get_hours_worked_on_date(date2), 1)
         self.assertEqual(staff_member.get_total_hours_working(), 11)

    def test_staff_at_minimum_hours(self):
        generic = CommonTestFunctions()

        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 10, 0, 0, 1, 1) # 4 hours
        duration2 = generic.duration(11, 17, 0, 0, 1, 1) # 6 hours
        duration3 = generic.duration(18, 19, 0, 0, 2, 2) # 1 hour
        duration4 = generic.duration(6, 14, 0, 0, 3, 3,) # 8 hours
        duration5 = generic.duration(14, 19, 0, 0, 3, 3) # 5 hours

        task1 = generic.task(group, location, category, duration1, 1)
        task2 = generic.task(group, location, category, duration2, 2)
        task3 = generic.task(group, location, category, duration3, 3)
        task4 = generic.task(group, location, category, duration4, 4)
        task5 = generic.task(group, location, category, duration5, 5)
        
        availability = [
            generic.availability(6,22, 1, 1),
            generic.availability(6,22, 2, 2),
            generic.availability(6,22, 3, 3),
            ]

        groups = [group]
        preferences = [generic.preference(category)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, min_hpw=5)

        self.assertFalse(staff_member.is_at_minimum_hours_per_week())
        self.assertFalse(staff_member.is_over_minimum_hours_per_week())

        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task2))
        self.assertFalse(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task1))
        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task5))

        self.assertTrue(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task2))
        self.assertFalse(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task1))
        self.assertFalse(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task5))

        self.assertFalse(staff_member.has_task(task1))
        self.assertFalse(staff_member.has_task(task2))
        self.assertFalse(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        staff_member.assign_task(task1) # + 4 hours, under minimum 

        self.assertFalse(staff_member.is_at_minimum_hours_per_week())
        self.assertFalse(staff_member.is_over_minimum_hours_per_week())

        self.assertRaises(AssertionError, staff_member.would_be_at_minimum_hours_if_task_was_assigned, task1)
        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task2))
        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task3))
        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task5))

        self.assertRaises(AssertionError, staff_member.would_be_over_minimum_hours_if_task_was_assigned, task1)
        self.assertTrue(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task2))
        self.assertFalse(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task3))
        self.assertTrue(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task5))

        self.assertTrue(staff_member.has_task(task1))
        self.assertFalse(staff_member.has_task(task2))
        self.assertFalse(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        staff_member.assign_task(task3)# + 1 hour, at minimum

        self.assertTrue(staff_member.is_at_minimum_hours_per_week())
        self.assertFalse(staff_member.is_over_minimum_hours_per_week())

        self.assertRaises(AssertionError, staff_member.would_be_at_minimum_hours_if_task_was_assigned, task1)
        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task2))
        self.assertRaises(AssertionError, staff_member.would_be_at_minimum_hours_if_task_was_assigned, task3)
        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_at_minimum_hours_if_task_was_assigned(task5))

        self.assertRaises(AssertionError, staff_member.would_be_over_minimum_hours_if_task_was_assigned, task1)
        self.assertTrue(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task2))
        self.assertRaises(AssertionError, staff_member.would_be_over_minimum_hours_if_task_was_assigned, task3)
        self.assertTrue(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_over_minimum_hours_if_task_was_assigned(task5))

        self.assertTrue(staff_member.has_task(task1))
        self.assertFalse(staff_member.has_task(task2))
        self.assertTrue(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

    def test_staff_at_target_hours(self):
        generic = CommonTestFunctions()

        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 13, 0, 0, 1, 1) # 7 hours
        duration2 = generic.duration(18, 19, 0, 0, 1, 1) # 1 hour
        duration3 = generic.duration(6, 8, 0, 0, 2, 2) # 2 hours
        duration4 = generic.duration(6, 14, 0, 0, 3, 3,) # 8 hours
        duration5 = generic.duration(14, 20, 0, 0, 4, 4) # 9 hours

        task1 = generic.task(group, location, category, duration1, 1)
        task2 = generic.task(group, location, category, duration2, 2)
        task3 = generic.task(group, location, category, duration3, 3)
        task4 = generic.task(group, location, category, duration4, 4)
        task5 = generic.task(group, location, category, duration5, 5)
        
        availability = [
            generic.availability(6,22, 1, 1),
            generic.availability(6,22, 2, 2),
            generic.availability(6,22, 3, 3),
            generic.availability(6,22, 4, 4),
            ]

        groups = [group]
        preferences = [generic.preference(category)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, min_hpw=5, target_hpw=8)

        self.assertFalse(staff_member.has_task(task1))
        self.assertFalse(staff_member.has_task(task2))
        self.assertFalse(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        self.assertFalse(staff_member.is_at_target_hours_per_week())
        self.assertFalse(staff_member.is_over_target_hours_per_week())

        staff_member.assign_task(task1) # + 7 hours 

        self.assertTrue(staff_member.has_task(task1))
        self.assertFalse(staff_member.has_task(task2))
        self.assertFalse(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        self.assertFalse(staff_member.is_at_target_hours_per_week())
        self.assertFalse(staff_member.is_over_target_hours_per_week())

        self.assertRaises(AssertionError, staff_member.would_be_at_target_hours_if_task_was_assigned, task1)
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task2))
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task3))
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task5))

        self.assertRaises(AssertionError, staff_member.would_be_over_target_hours_if_task_was_assigned, task1)
        self.assertFalse(staff_member.would_be_over_target_hours_if_task_was_assigned(task2))
        self.assertTrue(staff_member.would_be_over_target_hours_if_task_was_assigned(task3))
        self.assertTrue(staff_member.would_be_over_target_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_over_target_hours_if_task_was_assigned(task5))

        staff_member.assign_task(task2) # + 1 hour, at target

        self.assertTrue(staff_member.is_at_target_hours_per_week())
        self.assertFalse(staff_member.is_over_target_hours_per_week())

        self.assertTrue(staff_member.has_task(task1))
        self.assertTrue(staff_member.has_task(task2))
        self.assertFalse(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        self.assertRaises(AssertionError, staff_member.would_be_at_target_hours_if_task_was_assigned, task1)
        self.assertRaises(AssertionError, staff_member.would_be_at_target_hours_if_task_was_assigned, task2)
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task3))
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task5))

        self.assertRaises(AssertionError, staff_member.would_be_over_target_hours_if_task_was_assigned, task1)
        self.assertRaises(AssertionError, staff_member.would_be_over_target_hours_if_task_was_assigned, task2)
        self.assertTrue(staff_member.would_be_over_target_hours_if_task_was_assigned(task3))
        self.assertTrue(staff_member.would_be_over_target_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_over_target_hours_if_task_was_assigned(task5))

        staff_member.assign_task(task3) # + 2 hours, still over target

        self.assertTrue(staff_member.is_at_target_hours_per_week())
        self.assertTrue(staff_member.is_over_target_hours_per_week())

        self.assertTrue(staff_member.has_task(task1))
        self.assertTrue(staff_member.has_task(task2))
        self.assertTrue(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        self.assertRaises(AssertionError, staff_member.would_be_at_target_hours_if_task_was_assigned, task1)
        self.assertRaises(AssertionError, staff_member.would_be_at_target_hours_if_task_was_assigned, task2)
        self.assertRaises(AssertionError, staff_member.would_be_at_target_hours_if_task_was_assigned, task3)
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task4))
        self.assertTrue(staff_member.would_be_at_target_hours_if_task_was_assigned(task5))

    def test_staff_at_max_hours(self):
        generic = CommonTestFunctions()

        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 13, 0, 0, 1, 1) # 7 hours
        duration2 = generic.duration(18, 19, 0, 0, 1, 1) # 1 hour
        duration3 = generic.duration(6, 8, 0, 0, 2, 2) # 2 hours
        duration4 = generic.duration(6, 14, 0, 0, 3, 3,) # 8 hours
        duration5 = generic.duration(14, 20, 0, 0, 4, 4) # 9 hours

        task1 = generic.task(group, location, category, duration1, 1)
        task2 = generic.task(group, location, category, duration2, 2)
        task3 = generic.task(group, location, category, duration3, 3)
        task4 = generic.task(group, location, category, duration4, 4)
        task5 = generic.task(group, location, category, duration5, 5)
        
        availability = [
            generic.availability(6,22, 1, 1),
            generic.availability(6,22, 2, 2),
            generic.availability(6,22, 3, 3),
            generic.availability(6,22, 4, 4),
            ]

        groups = [group]
        preferences = [generic.preference(category)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, min_hpw=2, target_hpw=5, max_hpw=8)

        self.assertFalse(staff_member.has_task(task1))
        self.assertFalse(staff_member.has_task(task2))
        self.assertFalse(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        self.assertFalse(staff_member.is_at_maximum_hours_per_week())
        self.assertFalse(staff_member.is_over_maximum_hours_per_week())

        staff_member.assign_task(task1) # + 7 hours 

        self.assertTrue(staff_member.has_task(task1))
        self.assertFalse(staff_member.has_task(task2))
        self.assertFalse(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        self.assertFalse(staff_member.is_at_maximum_hours_per_week())
        self.assertFalse(staff_member.is_over_maximum_hours_per_week())

        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task1)
        self.assertTrue(staff_member.would_be_at_maximum_hours_if_task_was_assigned(task2))
        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task3)
        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task4)
        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task5)

        staff_member.assign_task(task2) # + 1 hour, at maximum

        self.assertTrue(staff_member.has_task(task1))
        self.assertTrue(staff_member.has_task(task2))
        self.assertFalse(staff_member.has_task(task3))
        self.assertFalse(staff_member.has_task(task4))
        self.assertFalse(staff_member.has_task(task5))

        self.assertTrue(staff_member.is_at_maximum_hours_per_week())
        self.assertFalse(staff_member.is_over_maximum_hours_per_week())

        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task1)
        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task2)
        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task3)
        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task4)
        self.assertRaises(AssertionError, staff_member.would_be_at_maximum_hours_if_task_was_assigned, task5)


if __name__ == '__main__':
    unittest.main()