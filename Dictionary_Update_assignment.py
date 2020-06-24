"""
program: Dictionary_Update_assignment.py
Author: Ondrea Li
Last date modfied: 06/24/20

The purpose of this program is to w
"""
score_dict = dict()
list = []
def get_test_scores():
    """
    Use reST style
    :param test_name: this represents the user's test name
    :param test_score: this represents test score
    :param invalid_message: this represents message if input invalid
    :return: test_name: test_score
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
    :param test_name: this represents the user's test name
    :param test_score: this represents test score
    :param invalid_message: this represents message if input invalid
    :return: average
    :raises keyError: raises an exception
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
        invalid_message = "Invalid score, try again"
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
