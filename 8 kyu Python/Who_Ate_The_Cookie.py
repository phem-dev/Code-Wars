"""
Instructions:
For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"
"""


# Solution:
def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif x == True:
        return "Who ate the last cookie? It was the dog!"
    else:
        return "Who ate the last cookie? It was Monica!"
