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
from app.models import AssignedTask, Task
from profile_assembler import ProfileAssembler

class AssignedTaskAssembler:
    def assemble(staff_members, schedule):
        assigned_tasks = []
        for member in staff_members:
            assigned_tasks.extend(AssignedTaskAssembler.translate(member, schedule))
        return assigned_tasks

    def translate(staff_member, schedule, user):
        all_database_tasks = Task.objects.all()
        staff_tasks = staff_member.get_tasks()
        profile = ProfileAssembler.assemble(staff_member)
        assigned_tasks = []
        for staff_task in staff_tasks:
            assigned_task = AssignedTask()
            assigned_task.schedule = schedule
            assigned_task.task = list(filter(lambda x: x.id == staff_task.id, all_database_tasks))[0]
            assigned_task.profile = profile
            date = staff_task.duration.start_time.date
            assigned_tasks.append(assigned_task)
        return assigned_tasks

