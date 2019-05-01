import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
sys.path.append(os.getcwd() + '\\..\\TestCommon')
from TestCommon import CommonTestFunctions
from staff_member import StaffMember


class TestStaffMember(unittest.TestCase):
    def setUp(self):
        self.good_staff_member = StaffMember(5, 'Bendan', 5, 10, 15, 8, [], [], [])

    def test_has_id(self):
        has_id = hasattr(self.good_staff_member, 'id')
        self.assertTrue(has_id)

    def test_has_name(self):
        has_name = hasattr(self.good_staff_member, 'name')
        self.assertTrue(has_name)

    #Minimum Hours Per Week
    #region 
    def test_set_minimum_hours_per_week(self):
        acceptable = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            12.5,
            ]

        unacceptable = [
            -10,
            -12.3245,
            168.1,
            170,
            200000,]

        for hour in acceptable:
            self._test_single_minimum_hours_per_week_passes(hour)

        for hour in unacceptable:
            self.assertRaises(AssertionError, self.good_staff_member.set_minimum_hours_per_week, hour)

    def _test_single_minimum_hours_per_week_passes(self, hour):
        try:
            self.good_staff_member.minimum_hours_per_week = hour
        except Exception as e:
            self.fail(e.args)
        else:
            self.assertEqual(self.good_staff_member.minimum_hours_per_week, hour)

    #endregion

    #Target Hours Per Week
    #region 
    def test_set_target_hours_per_week(self):
        minimum = 15
        maximum = 30
        staff_member = StaffMember(5, 'Brendan', minimum, 20, maximum, 8, [], [], [])

        acceptable = [
            minimum,
            minimum + 1,
            minimum + 2,
            minimum + 3,
            minimum + 4,

            maximum,
            maximum -1,
            maximum -2,
            maximum -3,
            maximum -4,

            minimum + 1.2,
            minimum + 4.6,
            ]

        unacceptable = [
            minimum -1,
            minimum -1.6,
            minimum - 100,
            maximum + 2,

            ]

        for hour in acceptable:
            self._test_single_target_hours_per_week_passes(hour)

        for hour in unacceptable:
            self.assertRaises(AssertionError, staff_member.set_target_hours_per_week, hour)

    def _test_single_target_hours_per_week_passes(self, hour):
        minimum = 15
        maximum = 30
        staff_member = StaffMember(5, 'Brendan', minimum, 20, maximum, 8, [], [], [])
        try:
            staff_member.target_hours_per_week = hour
        except Exception as e:
            self.fail(e.args)
        else:
            self.assertEqual(staff_member.target_hours_per_week, hour)

    #endregion

    #Maximum Hours Per Week
    #region 
    def test_set_maximum_hours_per_week(self):
        target = 20
        staff_member = StaffMember(5, 'Brendan', 15, target, 30, 8, [], [], [])

        acceptable = [
            target, 
            target + 1,
            target + 1.5,
            target + 2,
            target + 3,
            168
            ]

        unacceptable = [
            168.1,
            169,
            target - 1,
            target - 2,
            target - 6.235,
            ]

        for hour in acceptable:
            self._test_single_maximum_hours_per_week_passes(hour)

        for hour in unacceptable:
            self.assertRaises(AssertionError, staff_member.set_maximum_hours_per_week, hour)

    def _test_single_maximum_hours_per_week_passes(self, hour):
        minimum = 15
        maximum = 30
        staff_member = StaffMember(5, 'Brendan', minimum, 20, maximum, 8, [], [], [])
        try:
            staff_member.target_maximum_per_week = hour
        except Exception as e:
            self.fail(e.args)
        else:
            self.assertEqual(staff_member.target_maximum_per_week, hour)

    #endregion

    #Maximum Hours Per Day
    #region 
    def test_set_maximum_hours_per_day(self):
        staff_member = StaffMember(5, 'Brendan', 15, 20, 30, 8, [], [], [])

        acceptable = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            15.5,
            18.38505,
            ]

        unacceptable = [
            25.001,
            25,
            28,
            40000,
            -1,
            -1000,
            -16014,
            102,
            ]

        for hour in acceptable:
            self._test_single_maximum_hours_per_day_passes(hour)

        for hour in unacceptable:
            self.assertRaises(AssertionError, staff_member.set_maximum_hours_per_day, hour)

    def _test_single_maximum_hours_per_day_passes(self, hour):
        staff_member = StaffMember(5, 'Brendan', 15, 20, 30, 8, [], [], [])
        try:
            staff_member.target_maximum_per_day = hour
        except Exception as e:
            self.fail(e.args)
        else:
            self.assertEqual(staff_member.target_maximum_per_day, hour)

    #endregion
    
    def test_preference_cannot_work(self):
        generic = CommonTestFunctions()
        staff_member = generic.staff_member()
        cat_A = generic.category(id=1, name='A')
        cat_B = generic.category(id=2, name='B')
        cat_C = generic.category(id=3, name='C')
        cat_D = generic.category(id=4, name='D')

        pref_A = generic.preference(category=cat_A)
        pref_B = generic.preference(category=cat_B)
        pref_C = generic.preference(category=cat_C)
        pref_D = generic.preference(category=cat_D, can_work=False)

        preferences = [
            pref_A,
            pref_B,
            pref_C,
            pref_D,
            ]
        staff_member.preferences = preferences
        self.assertTrue(staff_member.can_work_in_category(cat_A))
        self.assertTrue(staff_member.can_work_in_category(cat_B))
        self.assertTrue(staff_member.can_work_in_category(cat_C))
        self.assertFalse(staff_member.can_work_in_category(cat_D))



if __name__ == '__main__':
    unittest.main()
