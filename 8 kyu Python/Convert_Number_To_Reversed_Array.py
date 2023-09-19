"""
Instructions:
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]
"""


# Solution:
def digitize(n):
    list = [int(i) for i in str(n)]
    return list[::-1]
