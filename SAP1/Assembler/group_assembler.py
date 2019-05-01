import os
import sys
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration')
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

class GroupAssembler:
    def assemble(database_groups):
        return list(map(GroupAssembler.parse_group, database_groups))

    def parse_group(group):
        return Group(group.id, group.name)
