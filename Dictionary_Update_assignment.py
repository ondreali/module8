"""
program: Dictionary_Update_assignment.py
Author: Ondrea Li
Last date modfied: 06/24/20

The purpose of this program is to write a function that ask for the number of test and test scores
to put it in a dictionary
and find the average score of the test scores
"""
score_dict = dict()
list = []
def get_test_scores():
    """
    Use reST style
    :param num_score: this represents the number of test scores
    :param score: this represents test score for each num_score
    :return score_dict
    :raises keyError: raises an exception
    """
    while True:
        try:
            num = num_score
            for test_name in range(1, num_score+1):
                score_dict[test_name] = list[test_name-1]
            return score_dict
        except ValueError as err:
            print("Value Error!", err)
            raise ValueError
def average_score(score_dict):
    """
    Use reST style
    :param list: this represents input for score
    :return: average score
    """
    num_score = len(list)
    score_total = 0
    for y in list:
        score_total += y
    average = score_total/num_score
    return average

if __name__ == '__main__':
    try:
        num_score = int(input("Enter the number of test scores: "))
        for n in range(0, num_score):
            score = int(input("Enter the test score: "))
            if 0 <= score and score <= 100:
                print("valid")
                list.append(score)
            else:
                print("Number must be in between 0 and 100")
    except ValueError as err:
        print("ValueError encountered")
        raise ValueError
    else:
        get_test_scores()
        print(score_dict)
        print("The average is",average_score(list))

