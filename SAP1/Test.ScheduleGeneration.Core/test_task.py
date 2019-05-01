import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\TestCommon')
from task import Task
from duration import Duration
from group import Group
from location import Location
from category import Category
from TestCommon import CommonTestFunctions
from bad_task_assignment_exception import BadTaskAssignmentException

class TestTask(unittest.TestCase):
    
    def setUp(self):
        start_time = datetime.datetime(2000, 1, 1, 6, 0)
        end_time = datetime.datetime(2000, 1, 1, 10, 0)
        self.duration = Duration(start_time, end_time)
        self.group = Group(0, 'TestGroup')
        self.location = Location(0, 'TestLoction')
        self.category = Category(0, 'TestCategory')
        self.good_task = Task(0, 'TestTask', self.duration, 3, self.group, self.location, self.category)

    def test_has_id(self):
        has_id = hasattr(self.good_task, 'id')
        self.assertTrue(has_id)
        self.assertEqual(0, self.good_task.id)

    def test_has_name(self):
        has_name = hasattr(self.good_task, 'name')
        self.assertTrue(has_name)
        self.assertEqual('TestTask', self.good_task.name)

    def test_has_duration(self):
        has_duration = hasattr(self.good_task, 'duration')
        self.assertTrue(has_duration)
        self.assertEqual(self.good_task.duration, self.duration)

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
            self.assertRaises(AssertionError, self.good_task.set_required_number_of_employees, number)

    def _test_single_required_number_of_employees(self, number):
        try:

            self.good_task.required_number_of_employees = number
        except Exception as e:
            self.fail(e.args)
        else:
            self.assertEqual(self.good_task.required_number_of_employees, number)

    def test_group(self):
        has_group = hasattr(self.good_task, 'group')
        self.assertTrue(has_group)
        self.assertEqual(self.good_task.group, self.group)

    def test_location(self):
        has_location = hasattr(self.good_task, 'location')
        self.assertTrue(has_location)
        self.assertEqual(self.good_task.location, self.location)

    def test_category(self):
        has_category = hasattr(self.good_task, 'category')
        self.assertTrue(has_category)
        self.assertEqual(self.good_task.category, self.category)

    def test_needed_staff(self):
        generic = CommonTestFunctions()
        required_number_of_employees = 5
        category = generic.category()
        location = generic.location()
        task_duration = generic.duration(9, 15)
        group = generic.group()
        task = generic.task(group, location, category, task_duration, required_number_of_employees=required_number_of_employees)

        availability = [generic.availability(6,22)]
        groups = [group]
        preferences = [generic.preference(category)]

        staff_member1 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
        staff_member2 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
        staff_member3 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
        staff_member4 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
        staff_member5 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
        staff_member6 = generic.staff_member(availability=availability, preferences=preferences, groups=groups)

        members = [
            staff_member1,
            staff_member2,
            staff_member3,
            staff_member4,
            staff_member5,
            staff_member6,
            ]
        assigned_staff_num = 0
        self.assertTrue(task.needs_staff([]))
        self.assertTrue(task.needs_staff(members))
        self.assertEqual(task.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(task.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(task.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(task.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(task.has_too_many_staff(members))
        self.assertFalse(task.has_too_many_staff([]))

        # Assign the task to a staff member 1 and increment the task. 
        staff_member1.assign_task(task)
        assigned_staff_num += 1
        
        self.assertTrue(task.needs_staff([]))
        self.assertTrue(task.needs_staff(members))
        self.assertEqual(task.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(task.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(task.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(task.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(task.has_too_many_staff(members))
        self.assertFalse(task.has_too_many_staff([]))

        # Assign the task to a staff member 2 and increment the task. 
        staff_member2.assign_task(task)
        assigned_staff_num += 1
        
        self.assertTrue(task.needs_staff([]))
        self.assertTrue(task.needs_staff(members))
        self.assertEqual(task.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(task.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(task.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(task.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(task.has_too_many_staff(members))
        self.assertFalse(task.has_too_many_staff([]))

        # Assign the task to a staff member 3 and increment the task. 
        staff_member3.assign_task(task)
        assigned_staff_num += 1
        
        self.assertTrue(task.needs_staff([]))
        self.assertTrue(task.needs_staff(members))
        self.assertEqual(task.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(task.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(task.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(task.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(task.has_too_many_staff(members))
        self.assertFalse(task.has_too_many_staff([]))

        # Assign the task to a staff member 4 and increment the task. 
        staff_member4.assign_task(task)
        assigned_staff_num += 1
        
        self.assertTrue(task.needs_staff([]))
        self.assertTrue(task.needs_staff(members))
        self.assertEqual(task.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(task.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(task.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(task.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(task.has_too_many_staff(members))
        self.assertFalse(task.has_too_many_staff([]))

        # Assign the task to a staff member 5 and increment the task. 
        staff_member5.assign_task(task)
        assigned_staff_num += 1
        
        self.assertTrue(task.needs_staff([]))

        # Note that this one is now false
        self.assertFalse(task.needs_staff(members)) 
        self.assertEqual(task.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(task.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(task.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(task.get_amount_of_needed_staff([]), required_number_of_employees)
        self.assertFalse(task.has_too_many_staff(members))
        self.assertFalse(task.has_too_many_staff([]))

        # There is no limit on how many staff can be assigned a task. Therefore, we can assign another member to the task 
        # and it should be allowed. 
        staff_member6.assign_task(task)
        assigned_staff_num += 1
        
        self.assertTrue(task.needs_staff([]))
        self.assertFalse(task.needs_staff(members)) 
        self.assertEqual(task.get_amount_of_assigned_staff(members), assigned_staff_num)
        self.assertEqual(task.get_amount_of_assigned_staff([]), 0)
        self.assertEqual(task.get_amount_of_needed_staff(members), required_number_of_employees - assigned_staff_num)
        self.assertEqual(task.get_amount_of_needed_staff([]), required_number_of_employees)

        # Now true
        self.assertTrue(task.has_too_many_staff(members))
        self.assertFalse(task.has_too_many_staff([]))

    def test_staff_who_can_take_this(self):
        generic = CommonTestFunctions()
        required_number_of_employees = 1
        category = generic.category()
        location = generic.location()
        task_duration = generic.duration(9, 15)
        group = generic.group()
        task = generic.task(group, location, category, task_duration, required_number_of_employees=required_number_of_employees)

        availability1 = [generic.availability(6,22)]
        availability2 = [generic.availability(9, 10)]
        groups = [group]
        preferences = [generic.preference(category)]

        staff_member1 = generic.staff_member(availability=availability1, preferences=preferences, groups=groups, id=1)
        staff_member2 = generic.staff_member(availability=availability1, preferences=preferences, groups=groups, id=2)
        staff_member3 = generic.staff_member(availability=availability2, preferences=preferences, groups=groups, id=3)

        staff_members = [
            staff_member1,
            staff_member2,
            staff_member3,
            ]

        self.assertTrue(staff_member1 in task.staff_who_can_take_this_task(staff_members))
        self.assertTrue(staff_member2 in task.staff_who_can_take_this_task(staff_members))
        self.assertFalse(staff_member3 in task.staff_who_can_take_this_task(staff_members))

        self.assertEqual(2, task.amount_of_staff_who_can_take_this_task(staff_members))

if __name__ == '__main__':
    unittest.main()
