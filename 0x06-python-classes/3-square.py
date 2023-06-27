#!/usr/bin/python3

"""define a class square"""


class Square:
    """a class Square that defines a square by: (based on 2-square.py)"""

    def __init__(self, size=0):
        """instanciate a class

        Args:
            size (int): ...
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Conpute a area"""

        return (self.__size**2)
