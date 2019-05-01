import os
import sys
import unittest
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\Assebler')
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
from role_assembler import RoleAssembler
from task_assembler import TaskAssembler
from category_assembler import CategoryAssembler

class TestCategoryAssembler(unittest.TestCase):
    def test_assembly(self):
        cat_id = 1
        cat_name = 'Category Test'
        database_category = DatabaseCategoryMock(cat_id, cat_name)

        scheduler_category = CategoryAssembler.assemble(database_category)
        self.assertEqual(scheduler_category.id, cat_id)
        self.assertEqual(scheduler_category.name, cat_name)

class DatabaseCategoryMock:
    def __init__(self, id, name, *args, **kwargs):
        self.id =id
        self.name = name
        return super().__init__(*args, **kwargs)

if __name__ == '__main__':
    unittest.main()