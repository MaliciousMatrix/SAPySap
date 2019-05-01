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
from task_assembler import TaskAssembler

class RoleAssembler:
    def assemble(database_roles):
        roles = []
        for r in database_roles:
            new_role = RoleAssembler.parse_role(r)
            roles.append(new_role)
        return roles

    def parse_role(database_role):
        tasks = TaskAssembler.assemble(database_role.tasks.all())
        return Role(database_role.id, database_role.name, tasks, database_role.number_of_employees_needed)