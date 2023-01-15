#!/usr/bin/python3
"""creating a method to add an attribute to a class"""


def add_attribute(obj, name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__setattr__(name, value)
