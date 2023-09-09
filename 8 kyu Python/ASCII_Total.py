"""
Instructions:
You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.

Examples:

uniTotal("a") == 97
uniTotal("aaa") == 291

"""


# Solution 1:
def uni_total(s):
    if len(s) == 1:
        return ord(s)
    elif len(s) > 1:
        total = 0
        for char in s:
            char = ord(char)
            total = total + char
        return total
    else:
        return 0


# Solution 2: Refactored
def uni_total(s):
    return sum(ord(char) for char in s)
