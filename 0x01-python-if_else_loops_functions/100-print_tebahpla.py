#!/usr/bin/python3
for char in range(122, 96, -1):
    print("{:c}".format(char if (char % 2 == 0) else (char - 32)), end='')
