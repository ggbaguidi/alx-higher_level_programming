#!/usr/bin/python3

"""define square"""


class Square:
    """a class Square that defines a square by: (based on 5-square.py)"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """to retrieve it"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """to set it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """to retrieve it"""

        return (self.__position)
    
    @position.setter
    def position(self, value):
        """to set it"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """a area"""

        return (self.__size**2)

    def my_print(self):
        """print a square"""

        for j in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" "*self.__position[0], end='')
            print("#"*self.__size)
