#!/usr/bin/python3
"""initialising a class square based on 2-square"""


class Square:
    """initialising the class"""
    def __init__(self, size=0):
        """initializing the class Square"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
