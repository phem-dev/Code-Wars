"""
Instructions:
Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained. 

Example
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is 9.
"""


# Solution 1:
def expression_matter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0
    elif a == 1 and b == 1 and c == 1:
        return 3
    elif a == 1 and b == 1:
        return a + b + c
    elif a == 1 and c == 1:
        return (a + b) * c
    elif b == 1 and c == 1:
        return a * (b + c)
    elif a == 1:
        return (a + b) * c
    elif b == 1:
        return max(a * (b + c), a + b + c)
    elif c == 1:
        return max(a * (b + c), a * b + c)
    else:
        return a * b * c


# Solution 2(refactored):
def expression_matter(a, b, c):
    return max(a * (b + c), a * b * c, (a + b) * c, a + b + c)
