#!/usr/bin/python3
"""Creates the class 'Student'."""


class Student:
    """the class called student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        if (isinstance(attr, list) and all(isinstance(ele, str)
                                           for ele in attr)):
            return {i: getattr(self, i) for i in attr if hasattr(self, i)}
        return self.__dict__
