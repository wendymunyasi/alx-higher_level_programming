#!/usr/bin/python3
from ast import Add
from audioop import add


if __name__ == "__main__":

    from sys import argv
    addition = 0

    number_of_args = len(argv)

    if number_of_args == 0:
        print(f"{addition:d}")
    for argument in argv:
        if argument != argv[0]:
            addition += int(argument)

    print("{}".format(addition))
