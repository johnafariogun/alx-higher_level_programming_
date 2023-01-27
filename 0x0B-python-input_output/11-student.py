#!/usr/bin/python3
"""initializes a class Student"""


class Student:
    """creates a class student with different public attributes"""

    def __init__(self, first_name, last_name, age):
        """
        args:
            first_name: first name of the student
            last_name: last name of the student
            age: the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dixtionary representation of a class"""
        dicts = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                dicts[i] = getattr(self, i)
        return dicts

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
