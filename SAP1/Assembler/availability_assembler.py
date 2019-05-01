import os
import sys
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Common')
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

class AvailabilityAssembler:
    def assemble(database_availabilities, database_days_off, current_date=datetime.datetime.now()):
        availability = []
        converter = DateConverter()
        for time in database_availabilities:
            day = time.get_day_as_string()
            start_time = time.start_time
            end_time = time.end_time
            duration = Availability(converter.create_duration_on_next_day(day, day, start_time, end_time, current_date))

            # Hack because the dateConverter isn't working properly but it'll work so we'll leave it. 
            if day == 'Sunday':
                duration.start_time = duration.start_time - timedelta(days=7)
                duration.end_time = duration.end_time - timedelta(days=7)

            availability.append(duration)

        for day_off in database_days_off:
            if not day_off.get_is_approved():
                continue

            date = day_off.day
            start_time = datetime.datetime(date.year, date.month, date.day, 0, 0)
            end_time = datetime.datetime(date.year, date.month, date.day, 23, 59)
            duration = Duration(start_time, end_time)
            to_remove = []
            for a in availability:
                if a.can_happen_inside_of(duration):
                    to_remove.append(a)

            for t in to_remove:
                availability.remove(t)

        return availability
