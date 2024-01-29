#!/usr/bin/python3
"""Creates the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Sets width, height, x, and y of rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns the area of the Rectangle instance"""
        area = self.width * self.height
        return area

    def display(self):
        """ Prints a square of hashes w given height and width"""
        h = self.height
        w = self.width
        for _ in range(self.y):
            print()
        for _ in range(h):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(w):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """ handle args """
        attr = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def __str__(self):
        """Returns string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
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
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
