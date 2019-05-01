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
from preference_assembler import PreferenceAssembler
from test_category_assembler import DatabaseCategoryMock
from category_assembler import CategoryAssembler
from role_assembler import RoleAssembler
from test_task_assembler import DatabaseTaskMock
from test_group_assembler import DatabaseGroupMock
from test_location_assembler import DatabaseLocationMock
from task_assembler import TaskAssembler


class TestRoleAssembler(unittest.TestCase):
    def test_assembly(self):

        role_name = 'Mock Role'
        role_id = 3
        req_emp_num = 2

        database_group = DatabaseGroupMock(1, 'Mock Group')
        database_location = DatabaseLocationMock(2, 'Location Mock', 'Fake addr')
        database_category = DatabaseCategoryMock(3, 'Category Mock')

        task1 = DatabaseTaskMock(1, 'Test Task 1', datetime.time(6, 30), 0, datetime.time(13), 0, database_group, database_location, database_category, 3)
        task2 = DatabaseTaskMock(2, 'Test Task 2', datetime.time(6, 30), 1, datetime.time(13), 1, database_group, database_location, database_category, 3)

        tasks = [
            task1,
            task2,
            ]

        database_role = DatabaseRoleMock(role_id, role_name, CollectionWrapper(tasks), req_emp_num)
        scheduler_role = RoleAssembler.parse_role(database_role)

        self.assertEqual(scheduler_role.id, role_id)
        self.assertEqual(scheduler_role.name, role_name)
        self.assertEqual(scheduler_role.tasks[0], TaskAssembler.parse_task(tasks[0]))
        self.assertEqual(scheduler_role.tasks[1], TaskAssembler.parse_task(tasks[1]))
        self.assertEqual(scheduler_role.required_number_of_employees, req_emp_num)
        



class DatabaseRoleMock:
    def __init__(self, id, name, tasks, number_of_employees_needed, *args, **kwargs):
        self.id = id
        self.name = name
        self.tasks = tasks
        self.number_of_employees_needed = number_of_employees_needed
        return super().__init__(*args, **kwargs)

class CollectionWrapper:
    def __init__(self, collection, *args, **kwargs):
        self.collection = collection
        return super().__init__(*args, **kwargs)
    
    def all(self):
        return self.collection

if __name__ == '__main__':
    unittest.main()