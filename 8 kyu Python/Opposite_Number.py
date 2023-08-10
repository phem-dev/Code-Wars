"""
Instructions:
Very simple, given an integer or a floating-point number, find its opposite.

Examples:

1: -1
14: -14
-34: 34

"""

# Solution:


def opposite(number):
    if number > 0:
        return -number
    elif number < 0:
        return (number - number) - number
    else:
        return 0
