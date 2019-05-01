import os
import sys
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
#sys.path.append(os.getcwd() + '\\..\\app')
from role import Role
#from .models import Role as DatabaseRole
from task import Task
from date_converter import DateConverter
from datetime import date, timedelta
import datetime
from duration import Duration
#from models import Task as DatabaseTask
from availability import Availability
from staff_member import StaffMember
from group import Group
from preference import Preference
from category import Category

class CategoryAssembler:
    def assemble(database_category):
        return Category(database_category.id, database_category.name)
