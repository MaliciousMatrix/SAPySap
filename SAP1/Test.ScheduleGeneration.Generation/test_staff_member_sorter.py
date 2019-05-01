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
from staff_member_sorter import StaffMemberSorter

class TestStaffMemberSorter(unittest.TestCase):
    def test_get_most_available_staff_members_for_tasks(self):
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

        availabilities1 = [generic.availability(6,7)]
        availabilities2 = [generic.availability(6,8)]
        availabilities3 = [generic.availability(6,9)]
        availabilities4 = [generic.availability(6, 10)]
        availabilities5 = [generic.availability(11,13)]
        groups = [group]

        member1 = generic.staff_member(availability = availabilities1, groups = groups, id=1) # Available for 1 task
        member2 = generic.staff_member(availability = availabilities3, groups = groups, id=2) # Available for 3 task
        member3 = generic.staff_member(availability = availabilities4, groups = groups, id=3) # Available for 4 tasks
        member4 = generic.staff_member(availability = availabilities5, groups = groups, id=4) # Available for 0 tasks
        member5 = generic.staff_member(availability = availabilities2, groups = groups, id=5) # Available for 2 tasks

        tasks = [
            task1,
            task2,
            task3,
            task4
            ]

        staff_members = [
            member1,
            member2,
            member3,
            member4,
            member5]

        staff_list = StaffMemberSorter.get_most_available_staff_members_for_tasks(tasks, staff_members, False)
        # Expected list = [member3, member2, member5, member1, member4]
        self.assertEqual(5, len(staff_list))
        self.assertEqual(member3, staff_list[0])
        self.assertEqual(member2, staff_list[1])
        self.assertEqual(member5, staff_list[2])
        self.assertEqual(member1, staff_list[3])
        self.assertEqual(member4, staff_list[4])
        self.assertEqual(StaffMemberSorter.get_most_available_staff_member(tasks, staff_members, False), member3)

        staff_list = StaffMemberSorter.get_least_available_staff_members_for_tasks(tasks, staff_members, False)
        # Expected list = [member4, member1, member5, member2, member3]
        self.assertEqual(5, len(staff_list))
        self.assertEqual(member4, staff_list[0])
        self.assertEqual(member1, staff_list[1])
        self.assertEqual(member5, staff_list[2])
        self.assertEqual(member2, staff_list[3])
        self.assertEqual(member3, staff_list[4])
        self.assertEqual(StaffMemberSorter.get_least_available_staff_member(tasks, staff_members, False), member4)

        staff_list = StaffMemberSorter.get_most_available_staff_members_for_tasks(tasks, staff_members, True)
        # Expected list = [member3, member2, member5, member1]
        self.assertEqual(4, len(staff_list))
        self.assertEqual(member3, staff_list[0])
        self.assertEqual(member2, staff_list[1])
        self.assertEqual(member5, staff_list[2])
        self.assertEqual(member1, staff_list[3])
        self.assertEqual(StaffMemberSorter.get_most_available_staff_member(tasks, staff_members, True), member3)

        staff_list = StaffMemberSorter.get_least_available_staff_members_for_tasks(tasks, staff_members, True)
        # Expected list = [member1, member5, member2, member3]
        self.assertEqual(4, len(staff_list))
        self.assertEqual(member1, staff_list[0])
        self.assertEqual(member5, staff_list[1])
        self.assertEqual(member2, staff_list[2])
        self.assertEqual(member3, staff_list[3])
        self.assertEqual(StaffMemberSorter.get_least_available_staff_member(tasks, staff_members, True), member1)

if __name__ == '__main__':
    unittest.main()