"""
Instructions:
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
"""


# Solution:
def reverse_seq(n):
    if n > 0:
        nums = [i for i in range(n + 1)]
        nums = nums[-1::-1]
        nums.pop()
        return nums
