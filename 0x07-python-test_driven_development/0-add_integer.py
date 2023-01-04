#!/usr/bin/python3
"""
add_integer
Defines an integer addition function that accepts floats and ints

"""


def add_integer(a, b=98):
    """Returns the integer additiion of a and b
    Raises:TypeError: if either a or b is not of int or float type.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
