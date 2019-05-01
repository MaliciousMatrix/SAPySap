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

class TestRole(unittest.TestCase):

    def setUp(self):
        start_time = datetime.datetime(2000, 1, 1, 6, 0)
        end_time = datetime.datetime(2000, 1, 1, 10, 0)
        self.duration = Duration(start_time, end_time)
        self.group = Group(0, 'TestGroup')
        self.location = Location(0, 'TestLoction')
        self.category = Category(0, 'TestCategory')
        good_tasks = [Task(0, 'TestTask', self.duration, 8, self.group, self.location, self.category)]
        generic = CommonTestFunctions()
        self.good_role = generic.role(good_tasks, name='Role', id=1)

    def test_has_id(self):
        has_id = hasattr(self.good_role, 'id')
        self.assertTrue(has_id)
        self.assertTrue(self.good_role.id, 1)

    def test_has_name(self):
        has_name = hasattr(self.good_role, 'name')
        self.assertTrue(has_name)
        self.assertEqual(self.good_role.name, 'Role')

    def test_task(self):
        generic = CommonTestFunctions()
        required_number_of_employees = 1
        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)

        task1 = generic.task(group, location, category, duration1, required_number_of_employees=required_number_of_employees, id=1)
        task2 = generic.task(group, location, category, duration2, required_number_of_employees=required_number_of_employees, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=required_number_of_employees, id=3)
        
        tasks = [
            task1,
            task2,
            task3
            ]

        role = Role(1, 'Role', tasks, 1)
        self.assertEqual(role.tasks[0], tasks[0])
        self.assertEqual(role.tasks[1], tasks[1])
        self.assertEqual(role.tasks[2], tasks[2])

    def test_cannot_give_conflicting_tasks(self):
        generic = CommonTestFunctions()
        required_number_of_employees = 1
        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)
        duration4 = generic.duration(6, 8)

        task1 = generic.task(group, location, category, duration1, required_number_of_employees=required_number_of_employees, id=1)
        task2 = generic.task(group, location, category, duration2, required_number_of_employees=required_number_of_employees, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=required_number_of_employees, id=3)
        task4 = generic.task(group, location, category, duration4, required_number_of_employees=required_number_of_employees, id=4)

        tasks = [
            task1,
            task2,
            task3,
            task4
            ]
        role = None

        try:
            role = Role(1, 'Role', tasks, required_number_of_employees)
        except AssertionError:
            pass
        else:
            raise Exception('Creating the role did not raise a conflicting task exception.')

    def test_req_num_emp_not_greater_than_minimum_task_req(self):
        generic = CommonTestFunctions()
        category = generic.category()
        location = generic.location()
        group = generic.group()

        duration1 = generic.duration(6, 7)
        duration2 = generic.duration(7, 8)
        duration3 = generic.duration(8, 9)

        task1 = generic.task(group, location, category, duration1, required_number_of_employees=2, id=1)
        task2 = generic.task(group, location, category, duration2, required_number_of_employees=4, id=2)
        task3 = generic.task(group, location, category, duration3, required_number_of_employees=3, id=3)

        tasks = [
            task1,
            task2,
            task3,
            ]

        acceptable = [
            1,
            2,
            ]
        unacceptable = [
            3,
            4,
            5,
            ]

        for a in acceptable:
            Role(1, 'Role', tasks, a)

        for u in unacceptable:
            try:
                Role(1, 'Role', tasks, u)
            except AssertionError:
                pass
            else:
                raise Exception('Creating a role with a bad req number of employees did not raise an exception. ' + str(u))

    def test_needs_staff(self):
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

        availability = [generic.availability(6,22)]
        groups = [group]
        preferences = [generic.preference(category)]

        staff_member1 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
        staff_member2 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
        staff_member3 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
        staff_member4 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)

        members = [
            staff_member1,
            staff_member2,
            staff_member3,
            staff_member4,
            ]

        assigned_staff_num = 0
        self.assertTrue(role.needs_staff([]))
        self.assertTrue(role.needs_staff(members))
        self.assertEqual(role.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(role.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(role.has_too_many_staff(members))
        self.assertFalse(role.has_too_many_staff([]))

        staff_member1.assign_role(role)
        assigned_staff_num += 1 # Total: 1

        self.assertTrue(role.needs_staff([]))
        self.assertTrue(role.needs_staff(members))
        self.assertEqual(role.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(role.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(role.has_too_many_staff(members))
        self.assertFalse(role.has_too_many_staff([]))

        staff_member2.assign_role(role)
        assigned_staff_num += 1 # Total: 2

        self.assertTrue(role.needs_staff([]))
        self.assertTrue(role.needs_staff(members))
        self.assertEqual(role.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(role.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(role.has_too_many_staff(members))
        self.assertFalse(role.has_too_many_staff([]))

        staff_member3.assign_role(role)
        assigned_staff_num += 1 # Total: 3

        self.assertTrue(role.needs_staff([]))
        self.assertFalse(role.needs_staff(members)) # Now False
        self.assertEqual(role.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(role.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(role.has_too_many_staff(members))
        self.assertFalse(role.has_too_many_staff([]))

        staff_member4.assign_role(role)
        assigned_staff_num += 1 # Total: 4

        self.assertTrue(role.needs_staff([]))
        self.assertFalse(role.needs_staff(members))
        self.assertEqual(role.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(role.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(role.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertTrue(role.has_too_many_staff(members)) # Now True
        self.assertFalse(role.has_too_many_staff([]))


    def test_staff_who_can_take_this_role(self):
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

        availability1 = [generic.availability(6,7)] # No
        availability2 = [generic.availability(6,22)] # Yes
        availability3 = [generic.availability(6,9)] # Yes
        availability4 = [generic.availability(5,10)] # Yes

        groups = [group]
        preferences = [generic.preference(category)]

        staff_member1 = generic.staff_member(availability=availability1, preferences=preferences, groups=groups, id=1) # No
        staff_member2 = generic.staff_member(availability=availability2, preferences=preferences, groups=groups, id=2) # Yes
        staff_member3 = generic.staff_member(availability=availability3, preferences=preferences, groups=groups, id=3) # Yes
        staff_member4 = generic.staff_member(availability=availability4, preferences=preferences, groups=groups, id=4) # Yes

        staff_members = [
            staff_member1,
            staff_member2,
            staff_member3,
            staff_member4,
            ]

        self.assertFalse(staff_member1 in role.staff_who_can_take_this_role(staff_members))
        self.assertTrue(staff_member2 in role.staff_who_can_take_this_role(staff_members))
        self.assertTrue(staff_member3 in role.staff_who_can_take_this_role(staff_members))
        self.assertTrue(staff_member4 in role.staff_who_can_take_this_role(staff_members))

        self.assertEqual(3, role.amount_of_staff_who_can_take_this_role(staff_members))


    def test_required_number_of_employees(self):
        acceptable = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            ]

        unacceptable = [
            0,
            -1,
            -10,
            -1003,
            -14562,
            -8.5,
            10.76,
            1.1,
            6.5,
            ]

        for number in acceptable:
            self._test_single_required_number_of_employees(number)

        for number in unacceptable:
            self.assertRaises(AssertionError, self.good_role.set_required_number_of_employees, number)

    def _test_single_required_number_of_employees(self, number):
        try:

            self.good_role.required_number_of_employees = number
        except Exception as e:
            self.fail(e.args)
        else:
            self.assertEqual(self.good_role.required_number_of_employees, number)


if __name__ == '__main__':
    unittest.main()
