#!/usr/bin/python3
"""Creates the class Rectangle"""


from base import Base
class Rectangle(Base):
    """ Sets width, height, x, and y of rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
       super().__init__(id) 
       self.__width = width
       self.__height = height
       self.__x = x
       self.__y = y
