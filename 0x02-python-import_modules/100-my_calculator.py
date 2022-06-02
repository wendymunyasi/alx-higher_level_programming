#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, mul, div, sub
    from sys import argv, exit

    # excludes name of file
    number_of_args = len(argv) - 1

    if number_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operat = argv[2]

    if operat != '+' and operat != '-' and operat != '*' and operat != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if operat == '+':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, add(a, b)))
    elif operat == '-':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, sub(a, b)))
    elif operat == '*':
        print("{:d} {} {:d} = {}".format(a, argv[2], b, mul(a, b)))
    else:
        print("{:d} {} {:d} = {}".format(a, argv[2], b, div(a, b)))
