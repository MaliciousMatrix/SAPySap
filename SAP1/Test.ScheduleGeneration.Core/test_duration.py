import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\TestCommon')
from TestCommon import CommonTestFunctions
from duration import Duration

class TestDuration(unittest.TestCase):

    def setUp(self):
        self.six_one_date = datetime.datetime(2000, 1, 1, 6, 0)
        self.ten_one_date = datetime.datetime(2000, 1, 1, 10, 0)
        self.six_two_date = datetime.datetime(2000, 1, 2, 6, 0)
        self.ten_two_date = datetime.datetime(2000, 1, 2, 10, 0)
        self.eleven_one_date = datetime.datetime(2000, 1, 1, 11, 0)
        self.seven_one_date = datetime.datetime(2000, 1, 1, 7, 0)
        self.nine_one_date = datetime.datetime(2000, 1, 1, 9, 0)

    def test_takes_start_and_end_time(self):
        start_time = self.six_one_date
        end_time = self.ten_one_date
        duration = Duration(start_time, end_time)
        self.assertEqual(duration.start_time, start_time)
        self.assertEqual(duration.end_time, end_time)

    def test_start_time_must_be_before_end_time(self):
        errenous_start_time = self.ten_one_date
        errenous_end_time = self.six_one_date

        # 10 am to 6 am on 1/1/2000 should raise exception 
        self.assertRaises(AssertionError, Duration, errenous_start_time, errenous_end_time)

        # 6 am to 6 am on 1/1/2000 should raise exception 
        self.assertRaises(AssertionError, Duration, errenous_start_time, errenous_start_time)

    def test_can_start_inside_of(self):

        six_to_eleven = Duration(self.six_one_date, self.eleven_one_date)
        six_to_ten = Duration(self.six_one_date, self.ten_one_date)
        seven_to_ten = Duration(self.seven_one_date, self.ten_one_date)

        self.assertTrue(six_to_ten.can_start_inside_of(six_to_eleven))
        self.assertTrue(six_to_ten.can_start_inside_of(six_to_ten))
        self.assertFalse(six_to_ten.can_start_inside_of(seven_to_ten))

    def test_can_end_inside_of(self):
        six_to_eleven = Duration(self.six_one_date, self.eleven_one_date)
        six_to_ten = Duration(self.six_one_date, self.ten_one_date)
        seven_to_ten = Duration(self.seven_one_date, self.ten_one_date)
        seven_to_nine = Duration(self.seven_one_date, self.nine_one_date)

        self.assertTrue(six_to_ten.can_end_inside_of(six_to_ten))
        self.assertTrue(six_to_ten.can_end_inside_of(seven_to_ten))
        self.assertTrue(six_to_ten.can_end_inside_of(six_to_eleven))
        self.assertFalse(six_to_ten.can_end_inside_of(seven_to_nine))

    def test_can_happen_inside_of(self):
        six_to_eleven = Duration(self.six_one_date, self.eleven_one_date)
        six_to_ten = Duration(self.six_one_date, self.ten_one_date)
        seven_to_ten = Duration(self.seven_one_date, self.ten_one_date)
        seven_to_nine = Duration(self.seven_one_date, self.nine_one_date)

        self.assertTrue(six_to_eleven.can_happen_inside_of(six_to_eleven))
        self.assertTrue(six_to_ten.can_happen_inside_of(six_to_eleven))
        self.assertFalse(six_to_eleven.can_happen_inside_of(six_to_ten))

        self.assertTrue(seven_to_nine.can_happen_inside_of(six_to_ten))
        self.assertFalse(six_to_ten.can_happen_inside_of(seven_to_nine))

        self.assertTrue(seven_to_ten.can_happen_inside_of(six_to_ten))
        self.assertFalse(six_to_ten.can_happen_inside_of(seven_to_ten))

    def test_conflicts_with(self):
        generic = CommonTestFunctions()
        six_to_ten = generic.duration(6, 10)
        five_to_eleven = generic.duration(5, 11)
        six_to_eleven = generic.duration(6, 11)
        five_to_ten = generic.duration(5, 10)
        ten_to_fifteen = generic.duration(10, 15)

        self.assertTrue(six_to_ten.conflicts_with(six_to_ten))
        self.assertTrue(six_to_ten.conflicts_with(five_to_eleven))
        self.assertTrue(six_to_ten.conflicts_with(six_to_eleven))
        self.assertTrue(six_to_ten.conflicts_with(five_to_ten))

        self.assertFalse(six_to_ten.conflicts_with(ten_to_fifteen))

    def test_get_length_in_hours(self):
        generic = CommonTestFunctions()

        four_hours = generic.duration(6, 10)
        self.assertEqual(four_hours.get_length_in_hours(), 4)

        four_andahalf_hours = generic.duration(5, 10, 30)
        self.assertEqual(four_andahalf_hours.get_length_in_hours(), 4.5)

    def test_is_on_date(self):
        generic = CommonTestFunctions()
        good_day = datetime.date(2000, 1, 1)
        bad_day = datetime.date(2000, 1, 2)
        duration = generic.duration()
        self.assertTrue(duration.is_on_date(good_day))
        self.assertFalse(duration.is_on_date(bad_day))

        good_date_time = datetime.datetime(2000, 1, 1, 4, 32)
        bad_date_time = datetime.datetime(2000, 1, 2, 4, 32)
        self.assertTrue(duration.is_on_date(good_date_time))
        self.assertFalse(duration.is_on_date(bad_date_time))

if __name__ == '__main__':
    unittest.main()