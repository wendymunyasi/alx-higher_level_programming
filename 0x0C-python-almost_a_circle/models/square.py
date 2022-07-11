#!/usr/bin/python3
"""Defines a class Square"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines properties of Square.

     Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
        id (int): identity of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Creates new instances of Square

        Args:
            size (int): width and height of square.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Property retriever for size.

        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square.

        Args:
            value (int): width of square.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be an integer")
        self.width = value
