"""
program: test_date_time
Author: Ondrea Li
Last date modfied: 06/23/20
The purpose of this program is to test half_birthday
"""
import datetime
import unittest
from more_fun_with_collections import half_birthday as hb

class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthdate = '2020-01-19'
        expected_date = '2020-07-19'
        self.assertEqual(expected_date, hb.half_birthday(birthdate))

if __name__ == '__main__':
    unittest.main()
