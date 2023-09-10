"""
Instructions:
Complete the square sum function so that it squares each number passed into it and then sums the results together.
"""


# Solution 1:
def square_sum(numbers):
    if len(numbers) > 1:
        total = 0
        for i in numbers:
            i = i**2
            total = total + i
        return total
    else:
        return 0


# SOlution2 (refactored):
def square_sum(numbers):
    return sum(i**2 for i in numbers)
