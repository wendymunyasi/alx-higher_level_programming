#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list

    Return a new list with True or False, depending on whether the integer,
    at the same position in the original list is a multiple of 2
    The new list should have the same size as the original list
    You are not allowed to import any module
    """

    list_length = len(my_list)
    new_list = []

    for num in range(list_length):
        if my_list[num] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
