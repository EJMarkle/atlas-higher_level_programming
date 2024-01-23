#!/usr/bin/python3
""" A function that writes an object to a text file,
    using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """writes obj to txt file w json"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
