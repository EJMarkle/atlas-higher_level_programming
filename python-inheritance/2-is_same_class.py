#!/usr/bin/python3
""" A function that checks if a given object is exactly
an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of
    the class, false if not
    """
    if type(obj) is a_class:
        return True
    else:
        return False
