# The ``2-matrix_divided`` module
============================================
How to use 2-matrix_divided.py
============================================

This library has one function called ``matrix_divided()``

``matrix_divided()`` returns a new matrix after a given matrix has been
divided by a number ``div``:

Importing the function matrix_divided.
    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Dividing by a positive or negative integer.
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 5)
    [[0.2, 0.4, 0.6], [0.8, 1.0, 1.2]]

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, -5)
    [[-0.2, -0.4, -0.6], [-0.8, -1.0, -1.2]]

    >>> matrix = [[1.1, 2, -3.3], [4, 5.5, -6]]
    >>> matrix_divided(matrix, 5)
    [[0.22, 0.4, -0.66], [0.8, 1.1, -1.2]]

    >>> matrix = [[1, 2.2, -3.3], [4.4, 5.5, -6]]
    >>> matrix_divided(matrix, -5)
    [[-0.2, -0.44, 0.66], [-0.88, -1.1, 1.2]]

Dividing by a positive or negative float.
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 2.2)
    [[0.45, 0.91, 1.36], [1.82, 2.27, 2.73]]

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, -2.2)
    [[-0.45, -0.91, -1.36], [-1.82, -2.27, -2.73]]

    >>> matrix = [[1.1, 2, -3.3], [4, 5.5, -6]]
    >>> matrix_divided(matrix, 5.5)
    [[0.2, 0.36, -0.6], [0.73, 1.0, -1.09]]

Dividing by 1
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 1)
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

Dividing by a boolean
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, True)
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, False)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

Dividing by a string.
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, "1")
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

Dividing by None.
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, None)
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

Dividing by a various types.
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, [1, 2])
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, {1})
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, ())
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, (1))
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

Dividing None by None.
    >>> matrix = None
    >>> matrix_divided(matrix, None)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing an empty matrix.
    >>> matrix = []
    >>> matrix_divided(matrix, 10)
    Traceback (most recent call last):
    	...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing a string as a matrix.
    >>> matrix = "chris brown"
    >>> matrix_divided(matrix, 10)
    Traceback (most recent call last):
    	...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing a tuple as a matrix.
    >>> matrix = ([1, 2, 3], [1, 2, 3])
    >>> matrix_divided(matrix, 10)
    Traceback (most recent call last):
    	...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Dividing a matrix where rows are unequal in size.
    >>> matrix = [[2, 34], [7, 9.8, -76, 1], [-77]]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size

Dividing a matrix where some of its elements are not floats or integers.
    >>> matrix = [[1, "2", 3], [{4}, "chris_breezy", (6)]]
    >>> matrix_divided(matrix, 10)
    Traceback (most recent call last):
    	...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing more than two arguments to matrix_divided().
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 10, 11) #doctest: +ELLIPSIS
    Traceback (most recent call last):
		...
    TypeError: matrix_divided() takes 2 positional arguments but ...

Passing no arguments to matrix_divided().
    >>> matrix_divided()
    Traceback (most recent call last):
        ...
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'

Passing one argument to matrix_divided().
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix)
    Traceback (most recent call last):
	    ...
    TypeError: matrix_divided() missing 1 required positional argument: 'div'
