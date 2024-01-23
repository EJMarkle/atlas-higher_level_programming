#!/usr/bin/python3
"""A function that returns a python object represented by a JSON string."""
import json


def from_json_string(my_str):
    """returns obj from json"""
    return json.loads(my_str)
