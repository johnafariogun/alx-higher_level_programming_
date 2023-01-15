#!/usr/bin/python3
"""creating a method to add an attribute to a class"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if possible
        Args:
            obj : the object, can be of any data type
            name: name of the attribute (str)
            value: value at the name (any)
        Raise:
            TypeError: if the attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__setattr__(name, value)
