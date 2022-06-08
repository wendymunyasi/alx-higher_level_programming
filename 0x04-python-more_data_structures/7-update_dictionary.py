#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary
    key argument will be always a string
    value argument will be any type
    If a key exists in the dictionary, the value will be replaced
    If a key doesn’t exist in the dictionary, it will be created
    You are not allowed to import any module
    """
    # a_dictionary[key] = value # or this

    a_dictionary.update([(key, value)])
    return a_dictionary
