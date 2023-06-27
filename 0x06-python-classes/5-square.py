#!/usr/bin/python3

"""define a class square"""


class Square:
    """a class Square that defines a square by: (based on 4-square.py)"""

    def __init__(self, size=0):
        """instanciate a class

        Args:
            size (int): ...
        """
        self.__size = size

    @property
    def size(self):
        """to retrieve it"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ to set it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Conpute a area"""

        return (self.__size**2)

    def my_print(self):
        """print asquare"""

        for i in range(self.__size):
            print("#"*self.__size)
        if self.__size == 0:
            print('')
