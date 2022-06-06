#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """print integers function

    One integer per line
    Don't import any module or cast integers to strings
    Assume the list only contains integers
    Use str.format() to print
    """
    if my_list:
        for integer in my_list:
            print("{:d}".format(integer))
