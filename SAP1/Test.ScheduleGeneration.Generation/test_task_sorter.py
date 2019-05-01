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
from task_sorter import TaskSorter

class TestTaskSorter(unittest.TestCase):
    def test_get_hardest_to_assign_tasks(self):
        generic = CommonTestFunctions()
        location = generic.location()

        category = generic.category(1, 'Cat One')

        group = generic.group(1, 'Group One')

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)
        duration4 = generic.duration(9, 10)


        task1 = generic.task(group, location, category, duration1, id=1)
        task2 = generic.task(group, location, category, duration2, id=2)
        task3 = generic.task(group, location, category, duration3, id=3)
        task4 = generic.task(group, location, category, duration4, id=4)
        
        availabilities67 = [generic.availability(6, 7)]
        availabilities78 = [generic.availability(7, 8)]
        availabilities89 = [generic.availability(8, 9)]
        groups = [group]

        member1 = generic.staff_member(availability = availabilities67, groups = groups, id=1) # Takes 1
        member2 = generic.staff_member(availability = availabilities67, groups = groups, id=2) # Takes 1
        member3 = generic.staff_member(availability = availabilities78, groups = groups, id=3) # Takes 3
        member4 = generic.staff_member(availability = availabilities78, groups = groups, id=4) # Takes 3
        member5 = generic.staff_member(availability = availabilities78, groups = groups, id=5) # Takes 3
        member6 = generic.staff_member(availability = availabilities89, groups = groups, id=6) # Takes 2

        staff_members = [
            member1,
            member2,
            member3,
            member4,
            member5,
            member6,
            ]

        tasks = [
            task1, # 2
            task2, # 3
            task3, # 1
            task4, # 0
            ]

        # Expected List = [task4, task3, task1, task2]
        task_list = TaskSorter.get_hardest_to_assign_tasks(tasks, staff_members, False)
        self.assertEqual(len(task_list), 4)
        self.assertTrue(task_list[0] == task4)
        self.assertTrue(task_list[1] == task3)
        self.assertTrue(task_list[2] == task1)
        self.assertTrue(task_list[3] == task2)
        self.assertEqual(TaskSorter.get_most_difficult_task_to_assign(tasks, staff_members, False), task4)

        # Expected List = [task3, task1, task2]
        task_list = TaskSorter.get_hardest_to_assign_tasks(tasks, staff_members, True)
        self.assertEqual(len(task_list), 3)
        self.assertTrue(task_list[0] == task3)
        self.assertTrue(task_list[1] == task1)
        self.assertTrue(task_list[2] == task2)
        self.assertEqual(TaskSorter.get_most_difficult_task_to_assign(tasks, staff_members, True), task3)


        # Expected List = [task2, task1, task3, task4]
        task_list = TaskSorter.get_easiest_to_assign_tasks(tasks, staff_members, False)
        self.assertEqual(len(task_list), 4)
        self.assertTrue(task_list[0] == task2)
        self.assertTrue(task_list[1] == task1)
        self.assertTrue(task_list[2] == task3)
        self.assertTrue(task_list[3] == task4)
        self.assertEqual(TaskSorter.get_easiest_task_to_assign(tasks, staff_members, False), task2)

        # Expected List = [task3, task1, task2]
        task_list = TaskSorter.get_easiest_to_assign_tasks(tasks, staff_members, True)
        self.assertEqual(len(task_list), 3)
        self.assertTrue(task_list[0] == task2)
        self.assertTrue(task_list[1] == task1)
        self.assertTrue(task_list[2] == task3)
        self.assertEqual(TaskSorter.get_easiest_task_to_assign(tasks, staff_members, True), task2)

if __name__ == '__main__':
    unittest.main()