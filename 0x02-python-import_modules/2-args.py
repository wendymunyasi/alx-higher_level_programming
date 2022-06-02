#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    count = 1

    # excludes name of program
    number_of_args = len(argv) - 1
    if number_of_args == 0:
        print(f"{number_of_args:d} arguments.")
    elif number_of_args == 1:
        print(f"{number_of_args:d} argument:")
        print(f"{number_of_args:d}: {argv[1]}")
    else:
        print(f"{number_of_args:d} arguments:")
    while count < len(argv):
        print(f"{count:d}: {argv[count]}")
        count += 1
