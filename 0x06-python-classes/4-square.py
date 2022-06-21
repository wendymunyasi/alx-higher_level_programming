#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 3-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
