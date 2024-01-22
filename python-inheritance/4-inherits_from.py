#!/usr/bin/python3
"""Checks if an object is an instance of a class that
inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if inherited, False if not"""
    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
