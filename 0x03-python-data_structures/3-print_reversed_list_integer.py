#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function that prints list in reverse

    One integer per line
    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers
    """

    if my_list:

        # point i to the last element
        i = len(my_list) - 1

        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1
