#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """function that replaces an element at specific position

    If idx is negative, the function should not modify anything, and
    returns the original list
    If idx is out of range (> of number of element in my_list), the
    function should not modify anything, and returns the original list
    You are not allowed to import any module
    You are not allowed to use try/except
    """

    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
