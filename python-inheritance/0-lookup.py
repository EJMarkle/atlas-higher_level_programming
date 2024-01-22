#!/usr/bin/python3
"""A function that returns a list of the available 
attributes and methods of an object.
"""


def lookup(obj):
    """returns attributes and methods of obj"""
    return dir(obj)