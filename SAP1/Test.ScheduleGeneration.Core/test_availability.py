import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
from availability import Availability
from TestCommon import CommonTestFunctions

class TestAvailability(unittest.TestCase):
    def test_start_time(self):
        generic = CommonTestFunctions()
        has_start_time = hasattr(generic.availability(), 'start_time')
        self.assertTrue(has_start_time)

    def test_end_time(self):
        generic = CommonTestFunctions()
        has_end_time = hasattr(generic.availability(), 'end_time')
        self.assertTrue(has_end_time)

if __name__ == '__main__':
    unittest.main()
