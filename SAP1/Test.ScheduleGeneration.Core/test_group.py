import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
from group import Group
from TestCommon import CommonTestFunctions

class TestGroup(unittest.TestCase):
    def test_equals(self):
        generic = CommonTestFunctions()
        a1 = generic.group(1, 'A')
        a2 = generic.group(2, 'A')
        b1 = generic.group(1, 'B')

        self.assertEqual(a1, a1)
        self.assertNotEqual(a1, b1)
        self.assertNotEqual(b1, a1)
        self.assertNotEqual(a1, a2)
        self.assertNotEqual(a2, a1)

    def test_has_id(self):
        generic = CommonTestFunctions()
        has_id = hasattr(generic.group(), 'id')
        self.assertTrue(has_id)

    def test_has_name(self):
        generic = CommonTestFunctions()
        has_name = hasattr(generic.group(), 'name')
        self.assertTrue(has_name)

if __name__ == '__main__':
    unittest.main()
