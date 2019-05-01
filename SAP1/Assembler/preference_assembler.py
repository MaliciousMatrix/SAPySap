import os
import sys
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
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
from category_assembler import CategoryAssembler

class PreferenceAssembler:
    def assemble(database_preferences):
        return list(map(PreferenceAssembler.parse_preference, database_preferences))

    def parse_preference(preference):
        can_work = preference.like != 0

        # This way neutral is 0, likes are positive and dislikes are negative. 
        likeness = preference.like - 3
        category = CategoryAssembler.assemble(preference.category)
        return Preference(category, likeness, can_work)