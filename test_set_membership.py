"""
program: test_set_membership
Author: Ondrea Li
Last date modfied: 06/23/20
The purpose of this program is to test set_membership
"""

import unittest
from more_fun_with_collections import set_membership as sm


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(sm.in_set("c"), True)


if __name__ == '__main__':
    unittest.main()
