#!/usr/bin/python3

def magic_calculation(a, b):
    """function that does exactly the same as the given Python bytecode.

    Args:
        a: integer
        b: integer
    """
    result = 0

    for num in range(1, 3):
        try:
            if num > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / num
        except Exception:
            result = b + a
            break
    return result
