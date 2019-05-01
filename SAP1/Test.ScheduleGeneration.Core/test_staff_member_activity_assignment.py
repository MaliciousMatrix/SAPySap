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

class TestStaffMemberActivity(unittest.TestCase):

    # Assigning Tasks
    #region 
    def test_assign_task(self):
        generic = CommonTestFunctions()

        category = generic.category()
        location = generic.location()
        task_duration = generic.duration(9, 15)
        group = generic.group()
        task = generic.task(group, location, category, task_duration)

        availability = [generic.availability(6,22)]
        groups = [group]
        preferences = [generic.preference(category)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups)

        self.assertFalse(staff_member.has_task(task), 'Staff member already had task! Something is broken with the test.')
        try:
            staff_member.assign_task(task)
        except BadTaskAssignmentException as e:
            self.fail('There was an exception while trying to assign a task to the member. Additional info: ' + str(e.args))

        self.assertTrue(staff_member.has_task(task), 'Staff member did not have the task after assignment!')

    def test_remove_task(self):
         generic = CommonTestFunctions()
         
         category = generic.category()
         location = generic.location()
         task_duration = generic.duration(10, 15)
         other_duration = generic.duration(15, 20)
         group = generic.group()
         task = generic.task(group, location, category, task_duration)
         other_task = generic.task(group, location, category, other_duration)
         
         availability = [generic.availability(6,22)]
         groups = [group]
         preferences = [generic.preference(category)]
         staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
         
         self.assertFalse(staff_member.has_task(task), 'Staff member already had task! Something is broken with the test.')
         self.assertFalse(staff_member.has_task(other_task), 'Staff member already had task! Something is broken with the test.')

         # Assign staff member both tasks.
         staff_member.assign_task(task)
         staff_member.assign_task(other_task)

         self.assertTrue(staff_member.has_task(task))
         self.assertTrue(staff_member.has_task(other_task))

         self.assertTrue(staff_member.can_remove_task(task))
         self.assertTrue(staff_member.can_remove_task(other_task))

         # remove the first task.
         staff_member.remove_task(task)

         self.assertFalse(staff_member.has_task(task))
         self.assertTrue(staff_member.has_task(other_task))

         self.assertFalse(staff_member.can_remove_task(task))
         self.assertTrue(staff_member.can_remove_task(other_task))

         # Try removing both tasks. This should remove other_task. 
         self.assertFalse(staff_member.try_remove_task(task))
         self.assertTrue(staff_member.try_remove_task(other_task))

         self.assertFalse(staff_member.has_task(other_task))
         self.assertFalse(staff_member.try_remove_task(other_task))
         self.assertFalse(staff_member.has_task(other_task))

    def test_clear_tasks(self):
        generic = CommonTestFunctions()
         
        category = generic.category()
        location = generic.location()
        task_duration = generic.duration(10, 15)
        other_duration = generic.duration(15, 20)
        group = generic.group()
        task = generic.task(group, location, category, task_duration)
        other_task = generic.task(group, location, category, other_duration)
         
        availability = [generic.availability(6,22)]
        groups = [group]
        preferences = [generic.preference(category)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups)
         
        self.assertFalse(staff_member.has_task(task), 'Staff member already had task! Something is broken with the test.')
        self.assertFalse(staff_member.has_task(other_task), 'Staff member already had task! Something is broken with the test.')

        # Assign staff member both tasks.
        staff_member.assign_task(task)
        staff_member.assign_task(other_task)

        self.assertTrue(staff_member.has_task(task))
        self.assertTrue(staff_member.has_task(other_task))

        # Remove all tasks. 
        staff_member.clear_tasks()

        self.assertFalse(staff_member.has_task(other_task))
        self.assertFalse(staff_member.has_task(other_task))

        # Remove all tasks again because we can. 
        staff_member.clear_tasks()

        self.assertFalse(staff_member.has_task(other_task))
        self.assertFalse(staff_member.has_task(other_task))

    def test_assign_task_with_bad_group(self):
        generic = CommonTestFunctions()

        category = generic.category()
        location = generic.location()
        task_duration = generic.duration(9, 15)
        task_group = generic.group(id=7, name='Task Group')
        task = generic.task(task_group, location, category, task_duration)

        staff_group = generic.group(id=8, name='Staff Group')
        availability = [generic.availability(6,22)]
        groups = [staff_group]
        preferences = [generic.preference(category)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups)

        self.assertRaises(BadTaskAssignmentException, staff_member.assign_task, task)
        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')
        self.assertFalse(staff_member.can_assign_task(task))
        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')
        self.assertFalse(staff_member.try_assign_task(task))
        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')

    def test_assign_task_with_cannot_work_in_category(self):
        generic = CommonTestFunctions()

        category = generic.category()
        location = generic.location()
        task_duration = generic.duration(9, 15)
        group = generic.group()
        task = generic.task(group, location, category, task_duration)

        availability = [generic.availability(6,22)]
        groups = [group]
        preferences = [generic.preference(category, can_work=False)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups)

        self.assertRaises(BadTaskAssignmentException, staff_member.assign_task, task)

        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')
        self.assertFalse(staff_member.can_assign_task(task))
        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')
        self.assertFalse(staff_member.try_assign_task(task))
        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')

    def test_assign_task_with_unavailable(self):
        generic = CommonTestFunctions()

        category = generic.category()
        location = generic.location()
        task_duration = generic.duration(11, 18)
        group = generic.group()
        task = generic.task(group, location, category, task_duration)

        availability = [generic.availability(6,10)]
        groups = [group]
        preferences = [generic.preference(category)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups)

        self.assertRaises(BadTaskAssignmentException, staff_member.assign_task, task)
        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')
        self.assertFalse(staff_member.can_assign_task(task))
        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')
        self.assertFalse(staff_member.try_assign_task(task))
        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')

    def test_assign_task_with_overlapping_task(self):
        generic = CommonTestFunctions()

        category = generic.category()
        location = generic.location()
        duration = generic.duration(6, 10)
        group = generic.group()
        task = generic.task(group, location, category, duration)

        availability = [generic.availability(6,22)]
        groups = [group]
        preferences = [generic.preference(category)]
        staff_member = generic.staff_member(availability=availability, preferences=preferences, groups=groups)

        self.assertFalse(staff_member.has_task(task), 'Staff member should not have the task!')
        try:
            staff_member.assign_task(task)
            self.assertTrue(staff_member.has_task(task))
        except:
            raise Exception('Something went wrong trying to assign a task to an open staff member. Test failure.')

        self.assertRaises(BadTaskAssignmentException, staff_member.assign_task, task)
        self.assertTrue(staff_member.has_task(task), 'Staff member did not have the task after assignment!')
        self.assertFalse(staff_member.can_assign_task(task))
        self.assertFalse(staff_member.try_assign_task(task))

    def test_tasks_this_can_take(self):
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

        availability1 = [generic.availability(6, 8)]
        groups = [group]
        preferences = [generic.preference(category)]

        staff_member1 = generic.staff_member(availability=availability1, preferences=preferences, groups=groups, id=1)
        takeable = staff_member1.tasks_this_can_take(tasks)

        self.assertEqual(3, len(takeable))
        self.assertTrue(task1 in takeable)
        self.assertTrue(task2 in takeable)
        self.assertFalse(task3 in takeable)
        self.assertTrue(task4 in takeable)

if __name__ == '__main__':
    unittest.main()