#!/usr/bin/python3
""" A function that checks if an object is an instance
    a specified class or inherited class. 
"""


def is_kind_of_class(obj, a_class):
    """Returns True if instance, False if not"""
    return isinstance(obj, a_class)
