"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.


def sublist(list_one, list_two):
    if list_one == list_two:
        return "EQUAL"
    if set(list_one).issubset(list_two):
        return "SUBLIST"
    if set(list_one).issuperset(set(list_two)):
        return "SUPERLIST"
    if set(list_one) != (set(list_two)):
        return "UNEQUAL"
    
print(sublist([1, 2, 3], [2, 3, 4]))