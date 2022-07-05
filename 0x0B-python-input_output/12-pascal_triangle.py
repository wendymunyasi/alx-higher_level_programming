#!/usr/bin/python3
"""Module containing the function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s,
    triangle of n.

    Args:
        n (int): rows of triangle.

    Returns:
        list: lists of lists of integers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0],
                                             [0] + pascal[-1])])
    return (pascal)
