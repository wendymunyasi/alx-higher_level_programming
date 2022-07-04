#!/usr/bin/python3
"""Returns a function lookup()"""


def lookup(obj):
    """Function that returns the list of available attributes and methods,
    f an object

    Args:
        obj (class): object

    Returns:
        list: list of available attributes and methods of an object
    """
    return dir(obj)
