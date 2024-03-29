#!/usr/bin/python3
""" Creates the 'Base' class"""
import json


class Base:
    """ Sets private class attribute and increments it if id is not None """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of 'list_dictionaries'"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of the JSON representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON representation of 'list_obj' to a file"""
        file = cls.__name__ + ".json"
        with open(file, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        elif cls.__name__ == "Square":
            temp = cls(1)

        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file = cls.__name__ + ".json"
        try:
            with open(file, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
