"""
Instructions:
Inspired by the development team at Vooza, write the function that

accepts the name of a programmer, and
returns the number of lightsabers owned by that person.
The only person who owns lightsabers is Zach, by the way. He owns 18, which is an awesome number of lightsabers. Anyone else owns 0.
"""


# Solution 1:
def how_many_light_sabers_do_you_own(name):
    if name == "Zach":
        return 18
    else:
        return 0


# Solution 2 (refactored):
def how_many_light_sabers_do_you_own(name):
    return 18 if name == "Zach" else 0
