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

    def to_json(self):
        """returns the dixtionary representation of a class"""
        return self.__dict__
