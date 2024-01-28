#!/usr/bin/python3
"""Creates the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Sets width, height, x, and y of rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        self.__y = value
