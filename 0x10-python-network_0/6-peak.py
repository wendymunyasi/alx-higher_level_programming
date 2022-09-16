#!/usr/bin/python3

def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    Returns:
        int: largest number in list
    """
    max_int = None
    for number in list_of_integers:
        if max_int is None or max_int < number:
            max_int = number
    return max_int
