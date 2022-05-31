#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        new_number = number * -1
        last_digit = (-1) * (new_number % 10)
        last_digit = last_digit * -1
    else:
        last_digit = number % 10

    print("{:d}".format(last_digit), end='')
    return last_digit
