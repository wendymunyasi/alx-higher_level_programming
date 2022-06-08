#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2
    You can assume that all values are only integers
    Returns a new dictionary
    You are not allowed to import any module
    """
    new_dict = a_dictionary.copy()
    dict_keys = list(new_dict.keys())

    for i in dict_keys:
        new_dict[i] *= 2

    return new_dict
