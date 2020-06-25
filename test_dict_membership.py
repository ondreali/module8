"""
program: test_dict_membership
Author: Ondrea Li
Last date modfied: 06/23/20
The purpose of this program is to test dict_membership
"""

import unittest
from more_fun_with_collections import dict_membership as dm


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertTrue(dm.in_dict("C"), True)
    def test_in_dict_false(self):
        self.assertFalse(dm.in_dict("P"), False)
    def test_in_set(self):
        self.assertTrue(dm.in_dict("D"), None)


if __name__ == '__main__':
    unittest.main()

