#!/usr/bin/python3
"""defines a function that returns a dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for
JSON serialization of an object"""


def class_to_json(obj):
    """returns the dixtionary representation of a class"""
    return obj.__dict__
