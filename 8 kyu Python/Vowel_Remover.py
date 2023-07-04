"""
Instructions:
reate a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
don't worry about uppercase vowels
y is not considered a vowel for this kata
"""

# Solution:


def shortcut(s):
    vowels = ["a", "e", "i", "o", "u"]

    result = [letter for letter in s if letter.lower() not in vowels]

    result = "".join(result)
    return result
