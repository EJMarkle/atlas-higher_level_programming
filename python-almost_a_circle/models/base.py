#!/usr/bin/python3
""" Creates the 'Base' class"""


class Base:
    """ Sets private class attribute and increments it if id is not None """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
