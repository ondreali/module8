"""
program: assign.averagey
Author: Ondrea Li
Last date modfied: 06/24/20

The purpose of this program is to write switch case statements using a function and a dictionary.
"""
def get_switch_value(average_score):
    """
    :returns: each return statement tells the user what grade they have
    :param average_score:
    :return:
    """
    returned_score = 0.0
def one():
    return "A"

def two():
    return "B"

def three():
    return "C"

def four():
    return "D"

def default():
    return "F"

def switch_average(grade_1, grade_2, grade_3):
    """
    Use reST style
    :param average_score: represents the average of the 3 grades
    :return : each return statement returns the average score to the dictionary
    """
    score_total = 0
    average_score = int(grade_1 + grade_2 + grade_3)/3

    if average_score >= 3.5:
        return one()
    if average_score >= 3:
        return two()
    if average_score >= 2.5:
        return three()
    if average_score >= 2:
        return four()
    if average_score <= 1.9:
        return default()




def switch(grades):
    """
    Use reST style
    :param grades: represents the argument
    :return a_func: returns to th
    """
    a_dict = {
        one(): "4.0",
        two(): "3.0",
        three(): "2.0",
        four(): "1.0",
        default(): "0.0",

    }

    a_func = a_dict.get(grades, "default")
    return a_func





if __name__ == "__main__":
    grade_1 = float(input("Enter score for test 1:"))
    grade_2 = float(input("Enter score for test 2:"))
    grade_3 = float(input("Enter score for test 3:"))
    average_score = switch_average(grade_1, grade_2, grade_3)
    print(average_score)
    get_switch_value(average_score)
    a_list_of_grades = 0






