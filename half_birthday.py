"""
program: Dictionary_Update_assignment.py
Author: Ondrea Li
Last date modfied: 06/24/20

The purpose of this program is to calculate half birthday
"""

import datetime
from datetime import timedelta

def half_birthday(birthdate):
    """
    Use reST style
    :param birthdate: represents birthdate
    :param half_birthday: represents when the calculated half birthday is
    :return returns calculated half birthday
    """
    birthdate_strp =startTime = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    half_birthday = birthdate_strp + timedelta(days = 183)
    return f'{half_birthday:%Y-%m-%d}'

if __name__ == '__main__':
    print(half_birthday('2020-01-19'))
