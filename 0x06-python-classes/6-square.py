#!/usr/bin/python3
"""initialising a class square based on 4-square"""


class Square:
    """initialising the class"""
    def __init__(self, size=0, position=(0, 0)):
        """initializing the class Square

        Args:
            size (int): size to initialize the class Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def position(self):
        """getter funtion of position
        Reeturns: positions in the sqaure
        """
        return self.__position

    @position.setter
    def position(Self, position):
        """ setter function of position
            Args:
                position(tuple) positions in the square
        """
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            print("\n"*self.__position[1], end="")
            for i in range(0, self.size):
                print(" " * self.__position[0], end="")
                for j in range(0, self.__size):
                    print('#', end="")
                print("")
