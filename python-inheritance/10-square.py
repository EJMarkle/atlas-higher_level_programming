#!/usr/bin/python3
"""Creates the class 'Square' that inherits from 'Rectangle'"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates class"""
    def __init__(self, size):
        """initialize rectangle size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """returns area of square"""
        return self.__size * self.__size
