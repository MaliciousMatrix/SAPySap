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
from role_assembler import RoleAssembler
from task_assembler import TaskAssembler
from location_assembler import LocationAssembler

class TestLocationAssembler(unittest.TestCase):
    def test_assembly(self):
        location_id = 5
        location_name = 'Test Location'
        location_address = '25555 Location Address'
        database_location = DatabaseLocationMock(location_id, location_name, location_address)

        scheduler_location = LocationAssembler.assemble(database_location)
        self.assertEqual(scheduler_location.id, location_id)
        self.assertEqual(scheduler_location.name, location_name)
        self.assertEqual(scheduler_location.address, location_address)


class DatabaseLocationMock:
    def __init__(self, id, name, address, *args, **kwargs):
        self.id =id
        self.name = name
        self.address = address
        return super().__init__(*args, **kwargs)

if __name__ == '__main__':
    unittest.main()
