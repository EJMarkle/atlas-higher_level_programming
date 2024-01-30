#!/usr/bin/python3
""" The class 'Square' """
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class 'Square', which inherits from 'Rectangle'"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ Size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the square """
        attr = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value, in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary definition of Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
