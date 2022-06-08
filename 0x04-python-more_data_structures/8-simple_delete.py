#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary.
    key argument will be always a string
    If a key doesn’t exist, the dictionary won’t change
    You are not allowed to import any module
    """
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return a_dictionary
