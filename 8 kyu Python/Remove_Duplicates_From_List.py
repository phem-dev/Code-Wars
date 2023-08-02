"""
Instructions:
Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

"""


# Solution:
def distinct(seq):
    my_set = set(seq)
    return list(my_set)
