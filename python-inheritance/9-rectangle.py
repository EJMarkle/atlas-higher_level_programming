#!/usr/bin/python3
"""Creates the class 'Rectangle' that inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates the class"""
    def __init__(self, width, height):
        """Checks if width and height are greater than 0"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints area of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
