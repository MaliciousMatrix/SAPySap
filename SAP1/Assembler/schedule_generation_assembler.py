import os
import sys
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Generation')
sys.path.append(os.getcwd() + '\\..\\SAP1\app')
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
from staff_member_assembler import StaffMemberAssembler
from ScheduleGenerator import ScheduleGenerator
from settings_assembler import SettingsAssembler
from assigned_task_assembler import AssignedTaskAssembler
from schedule_assembler import ScheduleAssembler
from assigned_role_assembler import AssignedRoleAssembler

class ScheduleGenerationAssembler:

    roles = []
    tasks = []
    staff_members = []
    settings = None

    def assemble(self, profiles, template, scheduler_settings, schedule_name):
        self.roles = RoleAssembler.assemble(template.get_roles())
        self.tasks = TaskAssembler.assemble(template.get_tasks())
        self.settings = SettingsAssembler.assemble(scheduler_settings)
        self.staff_members = StaffMemberAssembler.assemble(profiles)

        generator = ScheduleGenerator(staff_members, roles, tasks)
        generator.schedule(self.settings, self.tasks, self.staff_members, self.roles)
        schedule = ScheduleAssembler.assemble(schedule_name)
        assigned_tasks = AssignedTaskAssembler.assemble(staff_members, schedule)
        for t in assigned_tasks:
            pass
            #t.save()
        #assigned_roles = AssignedRoleAssembler.assemble(staff_members, schedule)

        a = 5
