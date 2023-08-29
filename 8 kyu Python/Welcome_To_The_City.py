"""
Instructions:
Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.

Example:

['John', 'Smith'], 'Phoenix', 'Arizona'
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!
"""


# Solution:
def say_hello(name, city, state):
    fname = name[0]
    lname = name[1]
    if len(name) > 2:
        lname = name[1] + " " + name[2]
    return f"Hello, {fname} {lname}! Welcome to {city}, {state}!"
