import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
from named_with_id import NamedWithId

class TestNamedWithId(unittest.TestCase):
    def setUp(self):
        self.good = NamedWithId(0, 'Fred')
    # Name
    #region
    def test_name(self):
        good_names = [
            'Kevin H',
            'Kevin',
            'A',
            'AAAAAA',
            'kevin',
            'Dr. Cliff',
            '6969420',
            ]

        bad_names = [
            '',
            '       ',
            '\n       ',
            '\n',
            None
            ]

        for name in good_names:
            self._test_single_name_passes(name)

        for name in bad_names:
            self.assertRaises(AssertionError, self.good.set_name, name)

    def _test_single_name_passes(self, name):
        try:
            self.good.name = name
        except Exception as e:
            self.fail(e.args)
        else:
            self.assertEqual(self.good.name, name)
    #endregion Name


if __name__ == '__main__':
    unittest.main()