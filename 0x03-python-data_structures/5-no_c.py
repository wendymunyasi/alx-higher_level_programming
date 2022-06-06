#!/usr/bin/python3

def no_c(my_string):
    """function that removes all characters c and C from string

    The function should return the new string
    You are not allowed to import any module
    You are not allowed to use str.replace()
    """
    list_1 = ['c', 'C']

    new_str = my_string[:]
    new_str = "".join(i for i in my_string if i not in list_1)

    return new_str
