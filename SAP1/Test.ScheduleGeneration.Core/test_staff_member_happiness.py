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

class TestStaffMemberHappiness(unittest.TestCase):

    def test_get_preferences_of(self):
        generic = CommonTestFunctions()

        category1 = generic.category(1)
        category2 = generic.category(2)
        category3 = generic.category(3)
        category4 = generic.category(4)
        category5 = generic.category(5)
        category6 = generic.category(6)

        preference1 = generic.preference(category1, -2)
        preference2 = generic.preference(category2, -1)
        preference3 = generic.preference(category3, 0)
        preference4 = generic.preference(category4, 1)
        preference5 = generic.preference(category5, 2)
        preference6 = generic.preference(category6, 2)

        preferences = [
            preference1,
            preference2,
            preference3,
            preference4,
            preference5,
            preference6,
            ]

        staff_member = generic.staff_member(preferences=preferences)
        self.assertTrue(preference1 in staff_member.get_preferences_of(-2))
        self.assertTrue(preference2 in staff_member.get_preferences_of(-1))
        self.assertTrue(preference3 in staff_member.get_preferences_of(0))
        self.assertTrue(preference4 in staff_member.get_preferences_of(1))
        self.assertTrue(preference5 in staff_member.get_preferences_of(2))
        self.assertTrue(preference6 in staff_member.get_preferences_of(2))

        self.assertRaises(AssertionError, staff_member.get_preferences_of, -3)
        self.assertRaises(AssertionError, staff_member.get_preferences_of, 3)
        self.assertRaises(AssertionError, staff_member.get_preferences_of, 0.1)
        self.assertRaises(AssertionError, staff_member.get_preferences_of, 1.5)

        self.assertEqual(staff_member.preferences, preferences)

    def test_get_preference_for_category(self):
        generic = CommonTestFunctions()

        category1 = generic.category(1)
        category2 = generic.category(2)
        category3 = generic.category(3)
        category4 = generic.category(4)
        category5 = generic.category(5)
        category6 = generic.category(6)
        category7 = generic.category(7)

        preference1 = generic.preference(category1, -2)
        preference2 = generic.preference(category2, -1)
        preference3 = generic.preference(category3, -0)
        preference4 = generic.preference(category4, 1)
        preference5 = generic.preference(category5, 2)
        preference6 = generic.preference(category6, 2)

        preferences = [
            preference1,
            preference2,
            preference3,
            preference4,
            preference5,
            preference6,
            ]

        staff_member = generic.staff_member(preferences=preferences)

        self.assertEqual(staff_member.get_preference_for_category(category1), preference1.likness)
        self.assertEqual(staff_member.get_preference_for_category(category2), preference2.likness)
        self.assertEqual(staff_member.get_preference_for_category(category3), preference3.likness)
        self.assertEqual(staff_member.get_preference_for_category(category4), preference4.likness)
        self.assertEqual(staff_member.get_preference_for_category(category5), preference5.likness)
        self.assertEqual(staff_member.get_preference_for_category(category6), preference6.likness)
        self.assertEqual(staff_member.get_preference_for_category(category7), Preference.get_avg_likness())

        self.assertTrue(staff_member.has_preference_for_category(category1))
        self.assertTrue(staff_member.has_preference_for_category(category2))
        self.assertTrue(staff_member.has_preference_for_category(category3))
        self.assertTrue(staff_member.has_preference_for_category(category4))
        self.assertTrue(staff_member.has_preference_for_category(category5))
        self.assertTrue(staff_member.has_preference_for_category(category6))
        self.assertFalse(staff_member.has_preference_for_category(category7))

        location = generic.location()
        task_duration = generic.duration(9, 15)
        group = generic.group()

        task1 = generic.task(group, location, category1, task_duration)
        task2 = generic.task(group, location, category2, task_duration)
        task3 = generic.task(group, location, category3, task_duration)
        task4 = generic.task(group, location, category4, task_duration)
        task5 = generic.task(group, location, category5, task_duration)
        task6 = generic.task(group, location, category6, task_duration)
        task7 = generic.task(group, location, category7, task_duration)

        self.assertEqual(staff_member.get_preference_for_task(task1), preference1.likness)
        self.assertEqual(staff_member.get_preference_for_task(task2), preference2.likness)
        self.assertEqual(staff_member.get_preference_for_task(task3), preference3.likness)
        self.assertEqual(staff_member.get_preference_for_task(task4), preference4.likness)
        self.assertEqual(staff_member.get_preference_for_task(task5), preference5.likness)
        self.assertEqual(staff_member.get_preference_for_task(task6), preference6.likness)
        self.assertEqual(staff_member.get_preference_for_task(task7), Preference.get_avg_likness())

        self.assertTrue(staff_member.dislikes_task(task1))
        self.assertFalse(staff_member.likes_task(task1))

        self.assertTrue(staff_member.dislikes_task(task2))
        self.assertFalse(staff_member.likes_task(task2))

        self.assertFalse(staff_member.dislikes_task(task3))
        self.assertFalse(staff_member.likes_task(task3))

        self.assertTrue(staff_member.likes_task(task4))
        self.assertFalse(staff_member.dislikes_task(task4))

        self.assertTrue(staff_member.likes_task(task5))
        self.assertFalse(staff_member.dislikes_task(task5))

        self.assertTrue(staff_member.likes_task(task6))
        self.assertFalse(staff_member.dislikes_task(task6))

    def test_get_happiness(self):
        generic = CommonTestFunctions()

        category1 = generic.category(1)
        category2 = generic.category(2)
        category3 = generic.category(3)
        category4 = generic.category(4)
        category5 = generic.category(5)
        category6 = generic.category(6)
        category7 = generic.category(7)

        preference1 = generic.preference(category1, -2)
        preference2 = generic.preference(category2, -1)
        preference3 = generic.preference(category3, -0)
        preference4 = generic.preference(category4, 1)
        preference5 = generic.preference(category5, 2)
        preference6 = generic.preference(category6, 2)

        preferences = [
            preference1,
            preference2,
            preference3,
            preference4,
            preference5,
            preference6,
            ]

        availability = [
            generic.availability(6, 22, 1, 1),
            generic.availability(6, 22, 2, 2),
            generic.availability(6, 22, 3, 3),
            generic.availability(6, 22, 4, 4),
            generic.availability(6, 22, 5, 5),
            generic.availability(6, 22, 6, 6),
            generic.availability(6, 22, 7, 7),
            ]

        group = generic.group()
        groups = [group]
        staff_member = generic.staff_member(preferences=preferences, groups=groups, availability=availability)

        location = generic.location()
        task_duration1 = generic.duration(9, 10, 0, 0, 1, 1)
        task_duration2 = generic.duration(9, 10, 0, 0, 2, 2)
        task_duration3 = generic.duration(9, 10, 0, 0, 3, 3)
        task_duration4 = generic.duration(9, 10, 0, 0, 4, 4)
        task_duration5 = generic.duration(9, 10, 0, 0, 5, 5)
        task_duration6 = generic.duration(9, 10, 0, 0, 6, 6)
        task_duration7 = generic.duration(9, 10, 0, 0, 7, 7)
        task_duration8 = generic.duration(10, 11, 0, 0, 7, 7)

        task1 = generic.task(group, location, category1, task_duration1) # -
        task2 = generic.task(group, location, category2, task_duration2) # -
        task3 = generic.task(group, location, category3, task_duration3) # =
        task4 = generic.task(group, location, category4, task_duration4) # 1
        task5 = generic.task(group, location, category5, task_duration5) # 1
        task6 = generic.task(group, location, category6, task_duration6) # 1
        task7 = generic.task(group, location, category7, task_duration7) # =
        task8 = generic.task(group, location, category1, task_duration8) # -

        self.assertEqual(staff_member.get_happiness(), 0)

        staff_member.assign_task(task1)

        self.assertEqual(staff_member.get_happiness(), -1)

        self.assertTrue(task1 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task1 in staff_member.get_tasks_that_make_me_happy())

        staff_member.assign_task(task2)

        self.assertEqual(staff_member.get_happiness(), -2)

        self.assertTrue(task1 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task1 in staff_member.get_tasks_that_make_me_happy())

        self.assertTrue(task2 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task2 in staff_member.get_tasks_that_make_me_happy())

        staff_member.assign_task(task3)

        self.assertEqual(staff_member.get_happiness(), -2)

        self.assertTrue(task1 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task1 in staff_member.get_tasks_that_make_me_happy())

        self.assertTrue(task2 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task2 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_happy())

        staff_member.assign_task(task4)

        self.assertEqual(staff_member.get_happiness(), -1)

        self.assertTrue(task1 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task1 in staff_member.get_tasks_that_make_me_happy())

        self.assertTrue(task2 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task2 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task4 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task4 in staff_member.get_tasks_that_make_me_happy())

        staff_member.assign_task(task5)

        self.assertEqual(staff_member.get_happiness(), 0)

        self.assertTrue(task1 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task1 in staff_member.get_tasks_that_make_me_happy())

        self.assertTrue(task2 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task2 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task4 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task4 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task5 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task5 in staff_member.get_tasks_that_make_me_happy())

        staff_member.assign_task(task6)

        self.assertEqual(staff_member.get_happiness(), 1)

        self.assertTrue(task1 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task1 in staff_member.get_tasks_that_make_me_happy())

        self.assertTrue(task2 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task2 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task4 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task4 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task5 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task5 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task6 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task6 in staff_member.get_tasks_that_make_me_happy())

        staff_member.assign_task(task7)

        self.assertEqual(staff_member.get_happiness(), 1)

        self.assertTrue(task1 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task1 in staff_member.get_tasks_that_make_me_happy())

        self.assertTrue(task2 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task2 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task4 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task4 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task5 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task5 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task6 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task6 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task7 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task7 in staff_member.get_tasks_that_make_me_happy())

        staff_member.assign_task(task8)

        self.assertEqual(staff_member.get_happiness(), 0)

        self.assertTrue(task1 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task1 in staff_member.get_tasks_that_make_me_happy())

        self.assertTrue(task2 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task2 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task3 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task4 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task4 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task5 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task5 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task6 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertTrue(task6 in staff_member.get_tasks_that_make_me_happy())

        self.assertFalse(task7 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task7 in staff_member.get_tasks_that_make_me_happy())

        self.assertTrue(task8 in staff_member.get_tasks_that_make_me_unhappy())
        self.assertFalse(task8 in staff_member.get_tasks_that_make_me_happy())

if __name__ == '__main__':
    unittest.main()