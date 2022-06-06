#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers

    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers
    """

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if column != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][column]), end='')
        print()
