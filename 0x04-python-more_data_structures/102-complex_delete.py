#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary
    If the value doesn’t exist, the dictionary won’t change
    All keys having the searched value have to be deleted
    You are not allowed to import any module
    """

    keys_list = list(a_dictionary.keys())

    for key in keys_list:
        if value == a_dictionary.get(key):
            del a_dictionary[key]

    return a_dictionary
