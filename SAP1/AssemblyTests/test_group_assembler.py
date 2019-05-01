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
from group_assembler import GroupAssembler

class TestGroupAssembler(unittest.TestCase):
    def test_assembly(self):
        id = 1
        name = 'Manager'
        database_group = DatabaseGroupMock(id, name)

        scheduler_group = GroupAssembler.parse_group(database_group)
        self.assertEqual(id, scheduler_group.id)
        self.assertEqual(name, scheduler_group.name)

class DatabaseGroupMock:
    def __init__(self, id, name, *args, **kwargs):
        self.id = id
        self.name = name

if __name__ == '__main__':
    unittest.main()