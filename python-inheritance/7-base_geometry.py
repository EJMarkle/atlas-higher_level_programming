#!/usr/bin/python3
"""Creates a class called BaseGeometry."""


class BaseGeometry:
    """class called BaseGeometry"""
    def area(self):
        """area not yet implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Checks if integer and if int over 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
