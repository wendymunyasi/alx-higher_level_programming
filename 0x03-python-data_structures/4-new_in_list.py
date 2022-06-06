#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """function that replaces an element in list w/o modifying the list

    If idx is negative, return a copy of the original list
    If idx is out of range (> of number of element in my_list),
    return a copy of the original list
    You are not allowed to import any module
    You are not allowed to use try/except
    """

    if my_list:
        if idx < 0:
            return my_list
        elif idx > len(my_list) - 1:
            return my_list
        else:
            new_list = my_list[:]
            new_list[idx] = element
            return new_list
