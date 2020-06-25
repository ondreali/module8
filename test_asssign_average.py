"""
program: test_set_membership
Author: Ondrea Li
Last date modfied: 06/23/20
The purpose of this program is to assign_average.py
"""

import unittest
from more_fun_with_collections import assign_average as aa


class MyTestCase(unittest.TestCase):
    def test_grade_A(self):
        self.assertEqual(aa.switch_average(grade_1 = 4, grade_2 = 4, grade_3 = 4), 'A')
    def test_grade_A_one(self):
        self.assertEqual(aa.switch_average(grade_1 = 3.9, grade_2 = 3.9, grade_3 = 3.9), 'A')
    def test_grade_B(self):
        self.assertEqual(aa.switch_average(grade_1 = 3, grade_2 = 3, grade_3 = 3), 'B')
    def test_grade_C(self):
        self.assertEqual(aa.switch_average(grade_1 = 2.7, grade_2 = 2.7, grade_3 = 2.7), 'C')
    def test_grade_D(self):
        self.assertEqual(aa.switch_average(grade_1 = 2.6, grade_2 = 2.6, grade_3 = 2.6), 'D')
    def test_grade_F_one(self):
        self.assertEqual(aa.switch_average(grade_1 = 1, grade_2 = 1, grade_3 = 1), 'F')
    def test_grade_default_one(self):
        self.assertEqual(aa.switch_average(grade_1 = 0, grade_2 = 0, grade_3 = 0), 'F')
    def test_grade_default_two(self):
        self.assertEqual(aa.switch_average(grade_1 = 0.5, grade_2 = 0.5, grade_3 = 0.5), 'F')



if __name__ == '__main__':
    unittest.main()
