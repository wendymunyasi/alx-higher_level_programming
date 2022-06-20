#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.
    my_list can contain any type (integer, string, etc.)
    You have to use try: / except:
    You have to use "{:d}".format() to print as integer.
    You are not allowed to import any module.
    All integers have to be printed on the same line followed by a new line,
    - other type of value in the list must be skipped (in silence).
    You are not allowed to use len().

        Args:
            x: Number of elements to access in my_list.

        Returns: The real number of integers printed.
    """
    count = 0
    for item in range(x):
        if isinstance(my_list[item], int):
            try:
                print(my_list[item], end='')
            except IndexError:
                break
        else:
            continue
        count += 1
    print()
    return count
