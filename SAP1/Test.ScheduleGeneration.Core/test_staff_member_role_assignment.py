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
from bad_role_assignment_exception import BadRoleAssignmentException

class TestStaffMemberRole(unittest.TestCase):
    
    def test_assign_role(self):
        generic = CommonTestFunctions()
        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)

        task1 = generic.task(group, location, category, duration1, required_number_of_employees=4, id=1)
        task2 = generic.task(group, location, category, duration2, required_number_of_employees=4, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=3, id=3)

        tasks = [
            task1,
            task2,
            task3,
            ]

        required_number_of_employees = 3
        role = Role(1, 'Role', tasks, required_number_of_employees)

        availability = [generic.availability(6,22)] # Yes

        groups = [group]
        preferences = [generic.preference(category)]

        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, id=1)

        self.assertFalse(staff_member.has_role(role))

        try:
            staff_member.assign_role(role)
        except BadRoleAssignmentException as e:
            self.fail('There was an exception while trying to assign a task to the member. Additional info: ' + str(e.args))

        self.assertTrue(staff_member.has_role(role))
        for task in role.tasks:
            self.assertTrue(staff_member.has_task(task))

    def test_remove_role(self):
        generic = CommonTestFunctions()
        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)

        duration4 = generic.duration(10, 11)
        duration5 = generic.duration(11, 12)


        task1 = generic.task(group, location, category, duration1, required_number_of_employees=4, id=1)
        task2 = generic.task(group, location, category, duration2, required_number_of_employees=4, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=3, id=3)

        tasks1 = [
            task1,
            task2,
            task3,
            ]

        task4 = generic.task(group, location, category, duration4, required_number_of_employees=4, id=4)
        task5 = generic.task(group, location, category, duration5, required_number_of_employees=4, id=5)

        tasks2 = [
            task4,
            task5
            ]

        required_number_of_employees = 3
        role1 = Role(1, 'Role1', tasks1, required_number_of_employees)
        role2 = Role(2, 'Role2', tasks2, required_number_of_employees)

        availability = [generic.availability(6,22)]

        groups = [group]
        preferences = [generic.preference(category)]

        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, id=1)

        self.assertFalse(staff_member.has_role(role1))
        self.assertFalse(staff_member.has_role(role2))

        # Assign both roles.
        staff_member.assign_role(role1)
        staff_member.assign_role(role2)

        self.assertTrue(staff_member.has_role(role1))
        self.assertTrue(staff_member.has_role(role2))

        for task in role1.tasks:
            self.assertTrue(staff_member.has_task(task))

        for task in role2.tasks:
            self.assertTrue(staff_member.has_task(task))

        self.assertTrue(staff_member.can_remove_role(role1))
        self.assertTrue(staff_member.can_remove_role(role2))

        # Remove the first Role
        staff_member.remove_role(role1)

        self.assertFalse(staff_member.has_role(role1))
        self.assertTrue(staff_member.has_role(role2))

        for task in role1.tasks:
            self.assertFalse(staff_member.has_task(task))

        for task in role2.tasks:
            self.assertTrue(staff_member.has_task(task))

        self.assertFalse(staff_member.can_remove_role(role1))
        self.assertTrue(staff_member.can_remove_role(role2))

        # Try removing both roles. This should remove role2. 
        self.assertFalse(staff_member.try_remove_role(role1))
        self.assertTrue(staff_member.try_remove_role(role2))

        self.assertFalse(staff_member.has_role(role1))
        self.assertFalse(staff_member.has_role(role2))
        self.assertFalse(staff_member.try_remove_role(role2))

        for task in role1.tasks:
            self.assertFalse(staff_member.has_task(task))

        for task in role2.tasks:
            self.assertFalse(staff_member.has_task(task))

    def test_assign_role_with_bad_time(self):
        generic = CommonTestFunctions()
        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)

        task1 = generic.task(group, location, category, duration1, required_number_of_employees=4, id=1)
        task2 = generic.task(group, location, category, duration2, required_number_of_employees=4, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=3, id=3)

        tasks = [
            task1,
            task2,
            task3,
            ]

        role = Role(1, 'Role1', tasks, 3)

        availability = [generic.availability(6,8)]

        groups = [group]
        preferences = [generic.preference(category)]

        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, id=1)

        self.assertRaises(BadRoleAssignmentException, staff_member.assign_role, role)
        self.assertFalse(staff_member.has_role(role))
        self.assertFalse(staff_member.can_assign_role(role))
        self.assertFalse(staff_member.has_role(role))
        self.assertFalse(staff_member.try_assign_role(role))
        self.assertFalse(staff_member.has_role(role))

    def test_cannot_work_in_category(self):
        generic = CommonTestFunctions()
        category = generic.category()
        category2 = generic.category(1, 'Cat2')
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)

        task1 = generic.task(group, location, category, duration1, required_number_of_employees=4, id=1)
        task2 = generic.task(group, location, category2, duration2, required_number_of_employees=4, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=3, id=3)

        tasks = [
            task1,
            task2,
            task3,
            ]

        role = Role(1, 'Role1', tasks, 3)

        preferences = [generic.preference(category2, 1, False), generic.preference(category)]

        availability = [generic.availability(6,10)]

        groups = [group]

        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, id=1)

        self.assertRaises(BadRoleAssignmentException, staff_member.assign_role, role)
        self.assertFalse(staff_member.has_role(role))
        self.assertFalse(staff_member.can_assign_role(role))
        self.assertFalse(staff_member.has_role(role))
        self.assertFalse(staff_member.try_assign_role(role))
        self.assertFalse(staff_member.has_role(role))

    def test_with_bad_group(self):
        generic = CommonTestFunctions()
        category = generic.category()
        location = generic.location()
        group = generic.group()
        group2 = generic.group(1, 'Test2')

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)

        task1 = generic.task(group, location, category, duration1, required_number_of_employees=4, id=1)
        task2 = generic.task(group2, location, category, duration2, required_number_of_employees=4, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=3, id=3)

        tasks = [
            task1,
            task2,
            task3,
            ]

        role = Role(1, 'Role1', tasks, 3)

        preferences = [generic.preference(category)]

        availability = [generic.availability(6,10)]

        groups = [group]

        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, id=1)

        self.assertRaises(BadRoleAssignmentException, staff_member.assign_role, role)
        self.assertFalse(staff_member.has_role(role))
        self.assertFalse(staff_member.can_assign_role(role))
        self.assertFalse(staff_member.has_role(role))
        self.assertFalse(staff_member.try_assign_role(role))
        self.assertFalse(staff_member.has_role(role))

    def test_roles_this_can_take(self):
        generic = CommonTestFunctions()
        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)

        duration4 = generic.duration(10, 11)
        duration5 = generic.duration(11, 12)

        duration6 = generic.duration(15, 16)
        duration7 = generic.duration(17, 18)


        task1 = generic.task(group, location, category, duration1, required_number_of_employees=4, id=1)
        task2 = generic.task(group, location, category, duration2, required_number_of_employees=4, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=3, id=3)

        tasks1 = [
            task1,
            task2,
            task3,
            ]

        task4 = generic.task(group, location, category, duration4, required_number_of_employees=4, id=4)
        task5 = generic.task(group, location, category, duration5, required_number_of_employees=4, id=5)

        tasks2 = [
            task4,
            task5
            ]

        task6 = generic.task(group, location, category, duration6, required_number_of_employees=4, id=6)
        task7 = generic.task(group, location, category, duration7, required_number_of_employees=4, id=7)

        tasks3 = [
            task6,
            task7,
            ]

        required_number_of_employees = 3
        role1 = Role(1, 'Role1', tasks1, required_number_of_employees) # Yes
        role2 = Role(2, 'Role2', tasks2, required_number_of_employees) # Yes
        role3 = Role(3, 'Role3', tasks3, required_number_of_employees) # No

        roles = [
            role1,
            role2,
            role3,
            ]

        availability = [generic.availability(6,12)]

        groups = [group]
        preferences = [generic.preference(category)]

        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups, id=1)
        takeable = staff_member.roles_this_can_take(roles)

        self.assertEqual(2, len(takeable))
        self.assertTrue(role1 in takeable)
        self.assertTrue(role2 in takeable)
        self.assertFalse(role3 in takeable)

if __name__ == '__main__':
    unittest.main()
