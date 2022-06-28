#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix.

Attributes:
    matrix_divided: divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): Value to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix isn't of the same size.
        TypeError: If an element of any list is not an integer or float.
        TypeError: If a row in the matrix is not a list.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        matrix: A result of the division.
    """
    row_size = None
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(message)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(message)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(message)

        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
