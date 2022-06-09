#!/usr/bin/python3

def value(roman):
    """returns value of each Roman symbol
    """
    if roman == 'I':
        return 1
    if roman == 'V':
        return 5
    if roman == 'X':
        return 10
    if roman == 'L':
        return 50
    if roman == 'C':
        return 100
    if roman == 'D':
        return 500
    if roman == 'M':
        return 1000
    return 0


def roman_to_int(roman_string):
    """converts a Roman numeral to an integer
    You can assume the number will be between 1 to 3999.
    def roman_to_int(roman_string) must return an integer
    If the roman_string is not a string or None, return 0
    """
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    result = 0
    i = 0

    while i < len(roman_string):
        # getting value of symbol roman_string[i]
        str1 = value(roman_string[i])

        if i + 1 < len(roman_string):
            # getting value of symbol roman_string[i + 1]
            str2 = value(roman_string[i + 1])

            # comparing both values
            if str1 >= str2:
                # Value of current symbol is greater
                # or equal to the next symbol
                result = result + str1
                i = i + 1
            else:
                # Value of current symbol is greater
                # or equal to the next symbol
                result = result + str2 - str1
                i = i + 2
        else:
            result = result + str1
            i = i + 1
    return result
