#!/usr/bin/python3
"""initialising a class square based on 4-square"""


class Square:
    """initialising the class"""
    def __init__(self, size=0):
        """initializing the class Square

        Args:
            size (int): size to initialize the class Square
        """
        self.size = size

    @property
    def size(self):
        """size method to retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, size_value):
        """ size method to set the size attribute to a value size_value
        Args:
            size_value (int): value to set the size attribute to
        """

        if type(size_value) is not int:
            raise TypeError("size must be an integer")

        elif size_value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size_value

    def area(self):
        """area method to calculate the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """my_print prints a square in # """
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print('#', end="")
                print("")
