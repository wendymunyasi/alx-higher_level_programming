#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Class that defines properties of Rectangle.

     Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates new instances of rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width retriever.

        Returns:
            int: width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of rectangle.

        Returns:
            int: width.
        """
        self.__width = value

    @property
    def height(self):
        """Height retriever.

        Returns:
            int: height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int): height of rectangle.

        Returns:
            int: height.
        """
        self.__height = value
