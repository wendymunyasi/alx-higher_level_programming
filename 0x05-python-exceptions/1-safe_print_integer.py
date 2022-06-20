#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().
    You have to use try: / except:
    You have to use "{:d}".format() to print as integer
    You are not allowed to import any module
    You are not allowed to use type()
        Args:
            value: integer to be printed.
        Returns: True if value has been correctly printed (it means the,
                 value is an integer). Otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
