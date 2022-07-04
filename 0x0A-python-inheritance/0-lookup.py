#!/usr/bin/python3
"""Returns a list of available attributes and methods of an object"""


def lookup(obj):
    method_list = [func for func in dir(obj) if callable(getattr(obj, func))]
    return method_list
    # return dir(obj)
