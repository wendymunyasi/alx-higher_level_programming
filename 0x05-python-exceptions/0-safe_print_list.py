#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    All elements must be printed on the same line followed by a new line.
    You have to use try: / except:
    You are not allowed to import any module
    You are not allowed to use len()
        Args:
            my_list: list
            x: number of elements to print.
        Returns: the real number of elements printed.
    """
    count = 0
    for item in range(x):
        try:
            print(my_list[item], end='')
        except IndexError:
            break
        else:
            count += 1
    print()
    return count
