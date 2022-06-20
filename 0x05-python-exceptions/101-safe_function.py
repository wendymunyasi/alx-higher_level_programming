#!/usr/bin/python3

def safe_function(fct, *args):
    """function that executes a function safely.

    Args:
        fct: assume fct will be always a pointer to a function.

    You have to use try: / except:

    Returns: The result of the function. Otherwise, returns None if,
    something happens during the function and prints in stderr the,
    error precede by Exception:

    """
    import sys

    try:
        result = fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
    return result
