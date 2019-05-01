import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
from preference import Preference
from category import Category
from TestCommon import CommonTestFunctions

class TestPreference(unittest.TestCase):

    def test_category(self):
        generic = CommonTestFunctions()
        acceptable = [
            generic.category(id=1, name='A'),
            generic.category(id=2, name='B'),
            generic.category(id=3, name='C'),
        ]

        for category in acceptable:
            p = None
            try:
                p = Preference(category, 0, True)
            except Exception as e:
                self.fail('Could not create preference. More Info: ' + str(e.args))
            else:
                self.assertEqual(p.category, category)

        self.assertRaises(AssertionError, Preference, None, 0, True)

    def test_likness(self):
        generic = CommonTestFunctions()
        category = generic.category()
        preference = generic.preference(category)

        has_likness = hasattr(preference, 'likness')
        self.assertTrue(has_likness)

        minimum = Preference.get_min_likness()
        maximum = Preference.get_max_likness() + 1
        possible_likeness_values = range(minimum, maximum)
        for val in possible_likeness_values:
            try:
                preference.likness = val
            except Exception as e:
                self.fail('failed to set preference to value: ' + str(val))
            else:
                self.assertEqual(preference.likness, val)

        unacceptable = [
            minimum -1,
            minimum -2,
            minimum -3,

            maximum +1,
            maximum +2,
            maximum +3,
            0.3,
            maximum - 0.3
            ]

        for val in unacceptable:
            self.assertRaises(AssertionError, preference.set_likness, val)

if __name__ == '__main__':
    unittest.main()
