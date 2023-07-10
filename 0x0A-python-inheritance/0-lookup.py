#!/usr/bin/python3
"""lookup"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return([x for x in dir(obj)])
