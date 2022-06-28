# The ``4-print_square`` module
============================================
How to use 4-print_square.py
============================================

This library has one function called ``print_square()``

``print_square()`` prints a square with the character #.

Importing the function print_square.
    >>> print_square = __import__('4-print_square').print_square

Passing an integer as size.
    >>> print_square(4)
    ####
    ####
    ####
    ####

Passing 0 as size.
    >>> print_square(0)

Passing non-integers as size.
    >>> print_square('4')
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square((1,))
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square(True)
    #

Passing a negative number as size.
    >>> print_square(-2)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0

Passing None as size.
    >>> print_square(None)
    Traceback (most recent call last):
    	...
    TypeError: size must be an integer

Passing a float as size.
    >>> print_square(4.4)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

Passing no argument to print_square().
    >>> print_square()
    Traceback (most recent call last):
   	    ...
    TypeError: print_square() missing 1 required positional argument: 'size'

Passing more than two arguments to print_square().
    >>> print_square(1, 2) #doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    TypeError: print_square() takes 1 positional argument but ...
