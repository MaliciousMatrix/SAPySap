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
from availability_assembler import AvailabilityAssembler
from preference_assembler import PreferenceAssembler
from group_assembler import GroupAssembler
from location_assembler import LocationAssembler
from category_assembler import CategoryAssembler

class TaskAssembler:
    def assemble(database_tasks):
        tasks = []
        for t in database_tasks:
            task = TaskAssembler.parse_task(t)
            tasks.append(task)

        return tasks

    def parse_task(t):
        converter = DateConverter()
        duration = converter.create_duration_on_next_day(t.get_start_day_string(), t.get_end_day_string(), t.start_time, t.end_time)
        group = GroupAssembler.parse_group(t.required_group)
        if t.location == None:
            location = None
        else:
            location = LocationAssembler.assemble(t.location)

        if t.category == None:
            category = None
        else:
            category = CategoryAssembler.assemble(t.category)

        return Task(t.id, t.task_name, duration, t.required_number_of_employees, group, location, category)