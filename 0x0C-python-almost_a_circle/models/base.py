#!/usr/bin/python3
"""define a Base class"""


class Base:
    """
    Args:
        id (int): id of object
    Return: a object base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instanciate a Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def nb_objects():
        """get a __nb_objects value"""
        return Base.__nb_objects
