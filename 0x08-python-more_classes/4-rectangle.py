#!/usr/bin/python3
"""
    declaring a class rectangle

"""


class Rectangle:
    """ a class rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ function that handles in the vlauation of the width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ function that handles in the vlauation of the heigth"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if (self.width == 0) or (self.height == 0):
            return (0)
        return (self.height * 2 + 2 * self.width)

    def __str__(self):
        if (self.width == 0) or (self.height) == 0:
            return('')
        rectangle = []
        for i in range(self.height):
            for j in range(self.width):
                rectangle.append('#')
            if i != self.height - 1:
                rectangle.append('\n')
        return (''.join(rectangle))

    def __repr__(self):
        """a string representation of the class called with width and height"""
        rectangle = 'Rectangle(' + str(self.width) + \
            ', ' + str(self.height) + ')'
        return (rectangle)
