#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

try:
    my_square = Rectangle.square(-2)
    print("{} / {}".format(my_square.width, my_square.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))