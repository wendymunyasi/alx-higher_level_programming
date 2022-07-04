#!/usr/bin/python3
"""Returns a list of available attributes and methods of an object"""


def lookup(obj):
    """Function that returns the list of available attributes and methods,
    f an object

    Args:
        obj (class): object

    Returns:
        list: list of available attributes and methods of an object
    """
    method_list = [func for func in dir(obj) if callable(getattr(obj, func))]
    return method_list
    # return dir(obj)
