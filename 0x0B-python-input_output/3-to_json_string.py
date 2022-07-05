#!/usr/bin/python3
"""Module containing the function to_json_string"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string).

    Args:
        my_obj (type): object to examine.

    Returns:
        str: JSON representation of object.
    """
    # print("type json.dumps(my_obj)--> {}".format(type(json.dumps(my_obj))))
    # print("type my_obj--> {}".format(type(my_obj)))

    # serializing json
    return json.dumps(my_obj)
