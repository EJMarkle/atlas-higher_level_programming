#!/usr/bin/python3
"""A function that adds two integers"""
def add_integer(a, b=98):
    """Returns the sum of a and b as an integer.
    Floats will be casted to integers, and raises
    a TypeError if neither.
    """
    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    if isinstance(a, int) and isinstance(b, int):
        return (a + b)
