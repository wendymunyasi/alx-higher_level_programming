#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys
    You can assume that all keys are strings
    Keys should be sorted by alphabetic order
    Only sort keys of the first level (don’t sort keys of a dictionary,
    inside the main dictionary)
    Dictionary values can have any type
    You are not allowed to import any module
    """

    dict_keys = list(a_dictionary.keys())
    dict_keys.sort()
    for i in dict_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
