#!/usr/bin/python3
"""creating a subclass that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """initial attributes and declarations"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()

    def __str__(self):
        """contains info about the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
