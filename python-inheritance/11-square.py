#!/usr/bin/python3
"""Creates the class Square, which inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates """

    def __init__(self, size):
        """initializing rectangle size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Prints the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
