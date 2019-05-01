import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\Assembler')
from duration import Duration
from date_converter import DateConverter

class TestDateConverter(unittest.TestCase):
    
    def setUp(self):
        self.sunday_date = datetime.date(2019, 1, 6)
        self.monday_date = datetime.date(2019, 1, 7)
        self.tuesday_date = datetime.date(2019, 1, 8)
        self.wednesday_date = datetime.date(2019, 1, 9)
        self.thursday_date = datetime.date(2019, 1, 10)
        self.friday_date = datetime.date(2019, 1, 11)
        self.saturday_date = datetime.date(2019, 1, 12)

    def test_date_to_int_conversion(self):
        converter = DateConverter()

        self.assertTrue(self.sunday_date.weekday() == converter.get_week_day_as_python_int('Sunday'))
        self.assertTrue(self.monday_date.weekday() == converter.get_week_day_as_python_int('Monday'))
        self.assertTrue(self.tuesday_date.weekday() == converter.get_week_day_as_python_int('Tuesday'))
        self.assertTrue(self.wednesday_date.weekday() == converter.get_week_day_as_python_int('Wednesday'))
        self.assertTrue(self.thursday_date.weekday() == converter.get_week_day_as_python_int('Thursday'))
        self.assertTrue(self.friday_date.weekday() == converter.get_week_day_as_python_int('Friday'))
        self.assertTrue(self.saturday_date.weekday() == converter.get_week_day_as_python_int('Saturday'))

        self.assertRaises(ValueError, converter.get_week_day_as_python_int, 'SGTSDFS')
        self.assertRaises(ValueError, converter.get_week_day_as_python_int, '')
        self.assertRaises(ValueError, converter.get_week_day_as_python_int, 'monday')
        self.assertRaises(ValueError, converter.get_week_day_as_python_int, 'hello')
        self.assertRaises(ValueError, converter.get_week_day_as_python_int, 'test')

    def test_convert(self):
        converter = DateConverter()

        expected_start_date = datetime.datetime(2019, 1, 14, 6, 0)
        expected_end_date = datetime.datetime(2019, 1, 14, 10, 0)
        self.__test_convert(expected_start_date, expected_end_date, 'Monday')

        expected_start_date = datetime.datetime(2019, 1, 15, 6, 0)
        expected_end_date = datetime.datetime(2019, 1, 15, 10, 0)
        self.__test_convert(expected_start_date, expected_end_date, 'Tuesday')

        expected_start_date = datetime.datetime(2019, 1, 16, 6, 0)
        expected_end_date = datetime.datetime(2019, 1, 16, 10, 0)
        self.__test_convert(expected_start_date, expected_end_date, 'Wednesday')

        expected_start_date = datetime.datetime(2019, 1, 17, 6, 0)
        expected_end_date = datetime.datetime(2019, 1, 17, 10, 0)
        self.__test_convert(expected_start_date, expected_end_date, 'Thursday')

        expected_start_date = datetime.datetime(2019, 1, 18, 6, 0)
        expected_end_date = datetime.datetime(2019, 1, 18, 10, 0)
        self.__test_convert(expected_start_date, expected_end_date, 'Friday')

        expected_start_date = datetime.datetime(2019, 1, 19, 6, 0)
        expected_end_date = datetime.datetime(2019, 1, 19, 10, 0)
        self.__test_convert(expected_start_date, expected_end_date, 'Saturday')

        expected_start_date = datetime.datetime(2019, 1, 20, 6, 0)
        expected_end_date = datetime.datetime(2019, 1, 20, 10, 0)
        self.__test_convert(expected_start_date, expected_end_date, 'Sunday')

    def __test_convert(self, expected_start_date, expected_end_date, day_string):
        converter = DateConverter()
        six = datetime.time(6,0)
        ten = datetime.time(10, 0)

        day_list = [
            self.sunday_date,
            self.monday_date,
            self.tuesday_date,
            self.wednesday_date,
            self.thursday_date,
            self.friday_date,
            self.saturday_date,
            ]

        for day in day_list:
            duration = converter.create_duration_on_next_day(day_string, day_string, six, ten, day)
            self.assertEqual(duration.start_time, expected_start_date)
            self.assertEqual(duration.end_time, expected_end_date)

if __name__ == '__main__':
    unittest.main()
