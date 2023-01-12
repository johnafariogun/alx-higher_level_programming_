#!/usr/bin/python3
"""module is ready :)"""


def inherits_from(obj, a_class):
    """checks if the obj is an instance that inherits from the class
    or another instance of the same class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
