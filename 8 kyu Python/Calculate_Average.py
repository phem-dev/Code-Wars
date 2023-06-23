"""
Instructions:
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.

"""


# Solution:
def find_average(numbers):
    total = sum(numbers)
    if numbers == []:
        return 0
    else:
        return total / len(numbers)


find_average([1, 2, 3])
find_average([])
