import unittest
import datetime
import sys
import os
sys.path.append(os.getcwd() + '\\..\\ScheduleGeneration.Core')
from has_unique_identifer import HasUniqueIdentifer

class A(HasUniqueIdentifer):
    pass

class B(HasUniqueIdentifer):
    pass

class TestHasUniqueIdentifer(unittest.TestCase):
    #Id
    #region 

    def setUp(self):
        self.good = HasUniqueIdentifer(0)

    def test_id(self):
        good_ids = [
            0,
            1,
            2,
            3,
            4,
            5,
            10000000,
            123423,
            ]
        bad_ids = [
            -1,
            -46104,
            -777777,
            12.3,
            -20.3,
            '10.31',
            'ssssss',
            '-10',
            ]

        for id in good_ids:
            self._test_single_id_passes(id)

        for id in bad_ids:
            self.assertRaises(AssertionError, self.good.set_id, id)

    def _test_single_id_passes(self, id):
        try:
            self.good.id = id
        except Exception as e:
            self.fail(e.args)
        else:
            self.assertEqual(self.good.id, id)

    #endregion

    def test_equals(self):
        one = HasUniqueIdentifer(1)
        two = HasUniqueIdentifer(2)
        self.assertEqual(one, one)
        self.assertEqual(two, two)
        self.assertNotEqual(one, two)
        self.assertNotEqual(two, one)

    def test_child_object_equal(self):
        a1 = A(1)
        a2 = A(2)
        b1 = B(1)
        h1 = HasUniqueIdentifer(1)

        self.assertNotEqual(a1, b1)
        self.assertNotEqual(a2, b1)
        self.assertNotEqual(h1, a1)
        self.assertNotEqual(h1, a2)
if __name__ == '__main__':
    unittest.main()
