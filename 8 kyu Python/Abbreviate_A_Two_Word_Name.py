"""
Instructions:
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

"""


# Solution:
def abbrev_name(name):
    first_name, last_name = name.split()
    initials = f"{first_name[0].upper()}.{last_name[0].upper()}"
    return initials
