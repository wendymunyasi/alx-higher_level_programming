#!/usr/bin/python3

def weight_average(my_list=[]):
    """ returns the weighted average of all integers tuple (<score>, <weight>)
    Returns 0 if the list is empty
    You are not allowed to import any module
    """
    if not my_list:
        return 0

    weight_sum = 0
    score_product = 0

    for sub in my_list:
        score_product += sub[0] * sub[1]
        weight_sum += sub[1]
    result = score_product / weight_sum

    return result
