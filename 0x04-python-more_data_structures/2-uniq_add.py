#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)
    You are not allowed to import any module
    """
    new_list = list(set(my_list))
    result = 0

    # -1 picks the last element in the returned list below
    return [result := result + num for num in new_list][-1]
