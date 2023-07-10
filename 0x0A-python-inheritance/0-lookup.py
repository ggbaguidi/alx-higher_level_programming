#/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """ A function lookup
    Args:
        obj (object):
    Return: a list object
    """
    return dir(obj)
