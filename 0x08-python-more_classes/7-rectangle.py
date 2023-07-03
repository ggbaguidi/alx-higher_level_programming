#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Representation of a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """returns printable string representation of rectangle as '#'"""
        string = ""
        if self.__width != 0 or self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns string representation of rectangle readable to computer"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """returns the number of objects remaining after a deletion"""
        print("Bye rectangle" + "." + "." + ".")
        Rectangle.number_of_instances -= 1
