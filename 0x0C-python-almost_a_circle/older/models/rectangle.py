#!/usr/bin/python3
from models.base import Base
"""define a rectangle class"""


class Rectangle(Base):
    """
    Args:
        width (int): width
        height (int): height
        x (int): x
        y (int): y
    Return: a object rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instanciate a class"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x muste be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __str__(self):
        """str"""
        return "[{obj}] ({id}) {x}/{y} - {width}/{height}".format(
            obj=type(self).__name__,
            id=self.id,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height
        )

    @property
    def width(self):
        """retrieve it"""
        return self.__width

    @width.setter
    def width(self, new_width):
        """set it"""
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")
        elif new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """retrieve it"""
        return self.__height

    @height.setter
    def height(self, new_height):
        """set it"""
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")
        elif new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """retrieve it"""
        return self.__x

    @x.setter
    def x(self, new_x):
        """set it"""
        if not isinstance(new_x, int):
            raise TypeError("x muste be an integer")
        elif new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """retrieve it"""
        return self.__y

    @y.setter
    def y(self, new_y):
        """set it"""
        if not isinstance(new_y, int):
            raise TypeError("y must be an integer")
        elif new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """the area"""
        return self.__width * self.__height

    def display(self):
        """Prints string representation of this rectangle."""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that updates instance attributes via */**args."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args."""
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
