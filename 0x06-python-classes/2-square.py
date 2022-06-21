#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines a square by: (based on 0-square.py)
    """
    def __init__(self, size=0):
        """Defines properties for the square

        Args:
            size: size of the square.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
