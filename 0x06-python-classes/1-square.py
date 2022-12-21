#!/usr/bin/python3
""" Creating a new class based on 0-square """


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Initialize square with a private size attribute"""
        self.__size = size
