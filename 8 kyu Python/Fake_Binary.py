"""
Instructions:
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
"""


# Solution:
def fake_bin(x):
    arr = ""
    for i in x:
        if i < "5":
            arr += "0"
        else:
            arr += "1"
    return arr
