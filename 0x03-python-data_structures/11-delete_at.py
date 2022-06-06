#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """function that deletes item at specific position in a list

    If idx is negative or out of range return the same list
    You are not allowed to use pop()
    You are not allowed to import any module
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    del my_list[idx]

    return my_list
