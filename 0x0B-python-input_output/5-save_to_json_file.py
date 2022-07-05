#!/usr/bin/python3
"""Module containing the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):

    # serializing json
    json_object = json.dumps(my_obj)

    # writing to file
    with open(filename, 'w') as f:
        return f.write(json_object)
