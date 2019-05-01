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
from app.models import Profile

class ProfileAssembler:
    def assemble(staff_member):
        return list(filter(lambda x: x.user.id == staff_member.id, Profile.objects.all()))[0]