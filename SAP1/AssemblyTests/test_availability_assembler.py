import os
import sys
import unittest
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


class TestAvailabilityAssembler(unittest.TestCase):
    def test_assembly(self):
        database_availabilities = [
            DatabaseAvailability(0, self.time(6), self.time(10)),
            DatabaseAvailability(1, self.time(11), self.time(15)),
            DatabaseAvailability(2, self.time(18), self.time(23)),
            DatabaseAvailability(3, self.time(6), self.time(22)),
            DatabaseAvailability(4, self.time(6), self.time(22)),
            DatabaseAvailability(5, self.time(6), self.time(22)),
            DatabaseAvailability(6, self.time(6), self.time(10)),
            DatabaseAvailability(6, self.time(12), self.time(18)),
            ]

        database_time_off_requests = [
            DatabaseDayOffRequest(self.date(4), 1),
            DatabaseDayOffRequest(self.date(5), 0),
            DatabaseDayOffRequest(self.date(6), 2),
            ]

        scheduler_availabilities = AvailabilityAssembler.assemble(database_availabilities, database_time_off_requests, datetime.date(2018, 6, 30))
        self.assertEqual(len(scheduler_availabilities), 7)
        
        self.assertEqual(scheduler_availabilities[0].start_time, self.date_time(1, 6, 0))
        self.assertEqual(scheduler_availabilities[1].start_time, self.date_time(2, 11, 0))
        self.assertEqual(scheduler_availabilities[2].start_time, self.date_time(3, 18, 0))
        self.assertEqual(scheduler_availabilities[3].start_time, self.date_time(5, 6, 0))
        self.assertEqual(scheduler_availabilities[4].start_time, self.date_time(6, 6, 0))
        self.assertEqual(scheduler_availabilities[5].start_time, self.date_time(7, 6, 0))
        self.assertEqual(scheduler_availabilities[6].start_time, self.date_time(7, 12, 0))

        self.assertEqual(scheduler_availabilities[0].end_time, self.date_time(1, 10, 0))
        self.assertEqual(scheduler_availabilities[1].end_time, self.date_time(2, 15, 0))
        self.assertEqual(scheduler_availabilities[2].end_time, self.date_time(3, 23, 0))
        self.assertEqual(scheduler_availabilities[3].end_time, self.date_time(5, 22, 0))
        self.assertEqual(scheduler_availabilities[4].end_time, self.date_time(6, 22, 0))
        self.assertEqual(scheduler_availabilities[5].end_time, self.date_time(7, 10, 0))
        self.assertEqual(scheduler_availabilities[6].end_time, self.date_time(7, 18, 0))

    def time(self, hour, minute=0):
        return datetime.time(hour, minute)

    def date(self, day):
        return datetime.date(2018, 7, day)

    def date_time(self, day, hour, minute):
        return datetime.datetime(2018, 7, day, hour, minute)

class DatabaseAvailability:
    def __init__(self, day, start_time, end_time, *args, **kwargs):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time

    def get_day_as_string(self):
        return self.DAY_CHOICES[self.day][1]

    DAY_CHOICES = (
		(0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
		(6, 'Saturday'),
        )
        

class DatabaseDayOffRequest:
    def __init__(self, date, state, *args, **kwargs):
        self.day = date
        self.state = state

    def get_is_approved(self):
        return self.state == 1;

if __name__ == '__main__':
    unittest.main()