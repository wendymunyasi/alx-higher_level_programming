#!/usr/bin/python3

def weight_average(my_list=[]):
    """ returns the weighted average of all integers tuple (<score>, <weight>)
    Returns 0 if the list is empty
    You are not allowed to import any module
    """
    if not my_list:
        return 0

    tuple_sum = 0
    for sub in my_list:
        tuple_sum += sum(sub)

    result = tuple_sum / len(my_list)

    return result
