"""
Instructions:
You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

"""


# Solution:
def two_sort(array):
    array.sort()
    first_string = array[0]
    result = "***".join(first_string)
    return result
