import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
from category import Category
from TestCommon import CommonTestFunctions

class TestCategory(unittest.TestCase):
    def test_equals(self):
        generic = CommonTestFunctions()
        a1 = generic.category(1, 'A')
        a2 = generic.category(2, 'A')
        b1 = generic.category(1, 'B')

        self.assertEqual(a1, a1)
        self.assertNotEqual(a1, b1)
        self.assertNotEqual(b1, a1)
        self.assertNotEqual(a1, a2)
        self.assertNotEqual(a2, a1)

    def test_has_id(self):
        generic = CommonTestFunctions()
        has_id = hasattr(generic.category(), 'id')
        self.assertTrue(has_id)

    def test_has_name(self):
        generic = CommonTestFunctions()
        has_name = hasattr(generic.category(), 'name')
        self.assertTrue(has_name)

if __name__ == '__main__':
    unittest.main()
