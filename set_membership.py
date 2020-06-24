"""
program: set_membership.py
Author: Ondrea Li
Last date modfied: 06/23/20

The purpose of this program is to accept and return a value stating if the element is in the set.

"""
x = set('abcdefg')
def in_set(type):
    # will accept a set and return a boolean value stating if the element is in the set

    """
    Use reST style
    : param x: set we are checking
    : param y: for the user to guess if it is in the set
    : return: return a boolean value stating if y, the element is in the set, x
    : raises keyError: raises an exception
    """
    try:
        y = type
        if y in x:
            print('True')
            return True
        else:
            print("false")
            return False
    except ValueError as err:
        print('error', err)
        raise ValueError

if __name__ == '__main__':
    type = input("guess set: ")
    set_input = in_set(type)



