#!/usr/bin/python3
""" creatinf an empty class BaseGeometry"""


class BaseGeometry:
    """creates an empty class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
