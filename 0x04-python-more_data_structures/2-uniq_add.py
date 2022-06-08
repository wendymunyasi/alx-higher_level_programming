#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)
    You are not allowed to import any module
    """
    # return [result := result + num for num in new_list][-1]

    new_list = list(set(my_list))
    result = 0

    for num in new_list:
        result += num
    return result
