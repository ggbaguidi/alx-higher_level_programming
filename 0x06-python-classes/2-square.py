#!/usr/bin/python3

"""define a square class"""


class Square:
    """a class Square that defines a square by: (based on 1-square.py)"""

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
