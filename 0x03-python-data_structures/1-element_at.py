#!/usr/bin/python3

def element_at(my_list, idx):
    """retrieve element function

    If idx is negative, the function should return None
    If idx is out of range (> of number of element in my_list), return None
    You are not allowed to import any module
    You are not allowed to use try/except
    """
    if my_list:
        if idx < 0:
            return
        elif idx > len(my_list) - 1:
            return
        else:
            return my_list[idx]
