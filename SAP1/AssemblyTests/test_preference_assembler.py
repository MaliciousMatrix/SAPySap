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

class TestPreferenceAssembler(unittest.TestCase):
    def test_assembly(self):
        category_id = 4
        category_name = 'Category Name'
        database_category = DatabaseCategoryMock(category_id, category_name)
        scheduler_category = CategoryAssembler.assemble(database_category)

        preference_like = 5
        database_preference = DatabasePreferenceMock(database_category, preference_like)
        scheduler_preference = PreferenceAssembler.parse_preference(database_preference)
        self.assertEqual(scheduler_preference.category, scheduler_category)
        self.assertEqual(scheduler_preference.likness, preference_like - 3)
        self.assertEqual(scheduler_preference.can_work, True)

        preference_like = 4
        database_preference = DatabasePreferenceMock(database_category, preference_like)
        scheduler_preference = PreferenceAssembler.parse_preference(database_preference)
        self.assertEqual(scheduler_preference.category, scheduler_category)
        self.assertEqual(scheduler_preference.likness, preference_like - 3)
        self.assertEqual(scheduler_preference.can_work, True)

        preference_like = 3
        database_preference = DatabasePreferenceMock(database_category, preference_like)
        scheduler_preference = PreferenceAssembler.parse_preference(database_preference)
        self.assertEqual(scheduler_preference.category, scheduler_category)
        self.assertEqual(scheduler_preference.likness, preference_like - 3)
        self.assertEqual(scheduler_preference.can_work, True)

        preference_like = 2
        database_preference = DatabasePreferenceMock(database_category, preference_like)
        scheduler_preference = PreferenceAssembler.parse_preference(database_preference)
        self.assertEqual(scheduler_preference.category, scheduler_category)
        self.assertEqual(scheduler_preference.likness, preference_like - 3)
        self.assertEqual(scheduler_preference.can_work, True)

        preference_like = 1
        database_preference = DatabasePreferenceMock(database_category, preference_like)
        scheduler_preference = PreferenceAssembler.parse_preference(database_preference)
        self.assertEqual(scheduler_preference.category, scheduler_category)
        self.assertEqual(scheduler_preference.likness, preference_like - 3)
        self.assertEqual(scheduler_preference.can_work, True)

        preference_like = 0
        database_preference = DatabasePreferenceMock(database_category, preference_like)
        scheduler_preference = PreferenceAssembler.parse_preference(database_preference)
        self.assertEqual(scheduler_preference.category, scheduler_category)
        self.assertEqual(scheduler_preference.likness, 0)
        self.assertEqual(scheduler_preference.can_work, False)

class DatabasePreferenceMock:
    def __init__(self, category, likness, *args, **kwargs):
        self.category = category
        self.like = likness
        return super().__init__(*args, **kwargs)

if __name__ == '__main__':
    unittest.main()
