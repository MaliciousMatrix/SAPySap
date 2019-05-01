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

class StaffMemberAssembler:

    def assemble(profiles):
        staff_members = []
        for p in profiles:
            member = StaffMemberAssembler.create_staff_member(p)
            staff_members.append(member)
        return staff_members

    def create_staff_member(profile):
        id = profile.id
        name = profile.get_name()
        minimum_hours_per_week = profile.minimum_hours_per_week
        target_hours_per_week = profile.target_hours_per_week
        maximum_hours_per_week = profile.maximum_hours_per_week
        maximum_hours_per_day = profile.maximum_hours_per_day
        availability = AvailabilityAssembler.assemble(profile.get_availabilities(), profile.get_days_off())
        preferences = PreferenceAssembler.assemble(profile.get_preferences())
        groups = GroupAssembler.assemble(profile.user.groups.all())

        staff_member = StaffMember(id, name, minimum_hours_per_week, target_hours_per_week, maximum_hours_per_week, maximum_hours_per_day, availability, preferences, groups)
        return staff_member