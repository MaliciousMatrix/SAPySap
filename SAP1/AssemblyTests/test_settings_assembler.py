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
from settings_assembler import SettingsAssembler


class TestSettingsAssembler(unittest.TestCase):
    def test_assembly(self):
        avoid_overtime = True
        start_overtime_at = 50
        take_preferences_into_account = False
        allow_split_shifts = True

        mock_settings = DatabaseSettingsMock(avoid_overtime, start_overtime_at, take_preferences_into_account, allow_split_shifts)
        scheduler_settings = SettingsAssembler.assemble(mock_settings)
        self.assertEqual(avoid_overtime, scheduler_settings.avoid_overtime)
        self.assertEqual(start_overtime_at, scheduler_settings.overtime_start_at)
        self.assertEqual(take_preferences_into_account, scheduler_settings.use_preferences)
        self.assertEqual(allow_split_shifts, scheduler_settings.allow_split_shifts)

        avoid_overtime = False
        start_overtime_at = 10
        take_preferences_into_account = True
        allow_split_shifts = False

        mock_settings = DatabaseSettingsMock(avoid_overtime, start_overtime_at, take_preferences_into_account, allow_split_shifts)
        scheduler_settings = SettingsAssembler.assemble(mock_settings)
        self.assertEqual(avoid_overtime, scheduler_settings.avoid_overtime)
        self.assertEqual(start_overtime_at, scheduler_settings.overtime_start_at)
        self.assertEqual(take_preferences_into_account, scheduler_settings.use_preferences)
        self.assertEqual(allow_split_shifts, scheduler_settings.allow_split_shifts)

class DatabaseSettingsMock:
    def __init__(self, avoid_overtime, start_overtime_at, take_preferences_into_account, allow_split_shifts, *args, **kwargs):
        self.avoid_overtime = avoid_overtime
        self.start_overtime_at = start_overtime_at
        self.take_preferences_into_account = take_preferences_into_account
        self.allow_split_shifts = allow_split_shifts
        return super().__init__(*args, **kwargs)

if __name__ == '__main__':
    unittest.main()