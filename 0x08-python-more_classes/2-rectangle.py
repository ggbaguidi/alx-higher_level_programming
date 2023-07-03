#!/usr/bin/python3
"""define rectangle 2"""


class Rectangle:
    """Write a class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """instanciate a class
        Args:
            width (int): ...
            height (int): ...
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """to retrieve it"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """to set it"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve it"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """to set it"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        """permeter of rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__height + self.__width) * 2)
