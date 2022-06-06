#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """function that adds two tuples

    Returns a tuple with 2 integers:
    The first element should be the addition of the first element of,
    each argument
    The second element should be the addition of the second element of,
    each argument
    You are not allowed to import any module
    You can assume that the two tuples will only contain integers
    If a tuple is smaller than 2, use the value 0 for each missing integer
    If a tuple is bigger than 2, use only the first 2 integers
    """

    tuple_a_length = len(tuple_a)
    tuple_b_lenth = len(tuple_b)

    if tuple_a_length == 0:
        a1 = 0
        a2 = 0
    elif tuple_a_length == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if tuple_b_lenth == 0:
        b1 = 0
        b2 = 0
    elif tuple_b_lenth == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    new_tuple = (a1 + b1, a2 + b2)

    return (new_tuple)
