#!/usr/bin/python3
"""Module defining the class Student based on 10-student.py"""


class Student:
    """
    Class that defines properties of student.

    Attributes:
        first_name (str): first name of student.
        last_name (int): last name of student.
        age (int): age of student.
    """
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Student.

        Args:
            first_name (str): first name of student.
            last_name (int): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in,
        this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Returns:
            dict: dictionary representation.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): json object.
        """
        # print("Type json --> {}".format(type(json)))
        self.__dict__.update(json)
