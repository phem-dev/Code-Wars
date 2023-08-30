"""
Instructions:
Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

"""


# Solution:
def print_array(arr):
    return ",".join(map(str, arr))
