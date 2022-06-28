#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square((True))
print("first")
print_square(10)
print("second")
print_square(0)
print("third")
print_square(1)
print("fourth")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")



