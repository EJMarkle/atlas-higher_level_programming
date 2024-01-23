#!/usr/bin/python3
""" Creates a class called Rectangle that inherits
    from BaseGeometry
    """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates class 'Rectangle' and inherits 'BaseGeometry'"""
    def __init__(self, width, height):
        """checks if width and height are greater than 0"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
