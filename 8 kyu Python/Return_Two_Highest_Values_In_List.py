"""
Instructions:
In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.
"""


# Solution:
def two_highest(arg1):
    arg1.sort(reverse=True)
    return arg1[1:3]
