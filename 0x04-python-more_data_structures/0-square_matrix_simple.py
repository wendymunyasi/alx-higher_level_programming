#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix
    Matrix is a 2 dimensional array
    Returns a new matrix: Same size as matrix, Each value should be,
    the square of the value of the input
    Initial matrix should not be modified
    You are not allowed to import any module
    You are allowed to use regular loops, map, etc.
    """
    new_matrix = [[elem**2 for elem in inner] for inner in matrix]

    return new_matrix
