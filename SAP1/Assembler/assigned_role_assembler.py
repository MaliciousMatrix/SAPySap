import os
import sys
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Common')
sys.path.append(os.getcwd() + '\\..\\SAP1\app')

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
from app.models import AssignedTask, Task, AssignedRole, Role
from profile_assembler import ProfileAssembler

class AssignedRoleAssembler:
    def assemble(staff_members, schedule):
        assigned_roles = []
        for member in staff_members:
            assigned_roles.extend(AssignedRoleAssembler.translate(member, schedule))
        return assigned_tasks

    def translate(staff_member, schedule, user):
        all_database_roles = Role.objects.all()
        staff_roles = staff_member.get_roles()
        profile = ProfileAssembler.assemble(staff_member)
        assigned_tasks = []
        for staff_role in staff_roles:
            assigned_role = AssignedRole()

            assigned_task = AssignedTask()
            assigned_task.schedule = schedule
            assigned_task.task = list(filter(lambda x: x.id == staff_task.id, all_database_roles))[0]
            assigned_task.profile = profile
            date = staff_task.duration.start_time.date
            assigned_tasks.append(assigned_task)
        return assigned_tasks
