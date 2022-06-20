#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists.

    Args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: length of list

    Returns: New list with all the divisions
    """
    new_list = []

    for item in range(list_length):
        try:
            quotient = my_list_1[item] / my_list_2[item]
        except IndexError:
            print("out of range")
            quotient = 0
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        finally:
            new_list.append(quotient)
    return new_list
