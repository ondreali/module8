"""
program: dict_membership
Author: Ondrea Li
Last date modfied: 06/23/20

The purpose of this program is to
"""
d = {'A':90, 'B':80, 'C':70, 'D': 60, 'F':0}
def in_dict(dict_key):
    """
    Use reST style
    :param d: this is the dictionary
    : param y: this is the element we are checking to see if it is in the dictionary
    : return: return a boolean value stating if y is in d.
    : raises keyError: raises an exception
    """
    try:
        y = dict_key
        if dict_key in d:
            print('True')
            return True
        else:
            print("false")
            return False
    except ValueError as err:
        print('error', err)
        raise ValueError

if __name__ == '__main__':
    type = input("What is your element:")
    in_dict(type)
