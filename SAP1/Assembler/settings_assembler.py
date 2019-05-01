import os
import sys
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Generation')
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
from availability_assembler import AvailabilityAssembler
from preference_assembler import PreferenceAssembler
from group_assembler import GroupAssembler
from scheduler_settings import SchedulerSettings

class SettingsAssembler:
    def assemble(database_settings):
        return SchedulerSettings(database_settings.avoid_overtime, database_settings.start_overtime_at, database_settings.take_preferences_into_account, database_settings.allow_split_shifts)
