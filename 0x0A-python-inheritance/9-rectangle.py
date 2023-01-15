#!/usr/bin/python3
"""creating a class that inherits from main class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """instantiating the sub class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ a method that finds the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """contains info about the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
