#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers

    You are not allowed to import any module
    You can assume that the list only contains integers
    You are not allowed to cast integers into strings
    You have to use str.format() to print integers
    """
    
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            print("{:d} ".format(matrix[row][column]), end='')
        print()
