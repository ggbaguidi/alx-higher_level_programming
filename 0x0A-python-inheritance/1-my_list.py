#!/usr/bin/python3
"""define a class MyList"""


class MyList(list):
    """Write a class MyList that inherits from list"""
    def __init__(self):
        """instanciate a class"""
        super().__init__()

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
