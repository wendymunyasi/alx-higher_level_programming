#!/usr/bin/python3
"""Module that reads a file and prints to stdout"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
