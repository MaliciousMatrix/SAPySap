import os
import sys
import unittest
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\Assembler')
#sys.path.append(os.getcwd() + '\\..\\app')
from role import Role
#from .models import Role as DatabaseRole
from task import Task
from date_converter import DateConverter
import datetime
from duration import Duration
#from models import Task as DatabaseTask
from availability import Availability
from staff_member import StaffMember
from group import Group
from preference import Preference
from task_assembler import TaskAssembler
from category_assembler import CategoryAssembler
from location_assembler import LocationAssembler
from group_assembler import GroupAssembler
from test_category_assembler import DatabaseCategoryMock
from category_assembler import CategoryAssembler
from test_location_assembler import DatabaseLocationMock
from test_group_assembler import DatabaseGroupMock
from test_category_assembler import DatabaseCategoryMock

class TestTaskAssembler(unittest.TestCase):
    def test_assembly(self):
        database_group = DatabaseGroupMock(1, 'Mock Group')
        database_location = DatabaseLocationMock(2, 'Location Mock', 'Fake addr')
        database_category = DatabaseCategoryMock(3, 'Category Mock')

        expected_group = GroupAssembler.parse_group(database_group)
        expected_location = LocationAssembler.assemble(database_location)
        expected_category = CategoryAssembler.assemble(database_category)

        task_id = 4
        task_name = 'Task Name'
        start_time = datetime.time(6, 30)
        end_time = datetime.time(13)
        required_num = 3
        database_task = DatabaseTaskMock(task_id, task_name, start_time, 0, end_time, 0, database_group, database_location, database_category, required_num)
        scheduler_task = TaskAssembler.parse_task(database_task)

        self.assertEqual(scheduler_task.category, expected_category)
        self.assertEqual(scheduler_task.group, expected_group)
        self.assertEqual(scheduler_task.location, expected_location)
        self.assertTrue(scheduler_task.duration.start_time.weekday() == 6)
        self.assertTrue(scheduler_task.duration.end_time.weekday() == 6)
        self.assertEqual(scheduler_task.id, task_id)
        self.assertEqual(scheduler_task.name, task_name)
        self.assertEqual(scheduler_task.duration.start_time.hour, start_time.hour)
        self.assertEqual(scheduler_task.duration.start_time.minute, start_time.minute)
        self.assertEqual(scheduler_task.duration.end_time.hour, end_time.hour)
        self.assertEqual(scheduler_task.duration.end_time.minute, end_time.minute)
        self.assertEqual(scheduler_task.required_number_of_employees, required_num)

class DatabaseTaskMock:
    def __init__(self, id, task_name, start_time, start_day, end_time, end_day, required_group, location, category, required_number_of_employees, *args, **kwargs):
        self.id = id
        self.task_name = task_name
        self.start_time = start_time
        self.start_day = start_day
        self.end_time = end_time
        self.end_day = end_day
        self.required_group = required_group
        self.location = location
        self.category = category 
        self.required_number_of_employees = required_number_of_employees

        return super().__init__(*args, **kwargs)
    DAY_CHOICES = (
		(0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
		(6, 'Saturday'),
        )

    def get_start_day_string(self):
        return self.__get_day_as_string(self.start_day)

    def get_end_day_string(self):
        return self.__get_day_as_string(self.end_day)

    def __get_day_as_string(self, day):
        return self.DAY_CHOICES[day][1]


if __name__ == '__main__':
    unittest.main()
