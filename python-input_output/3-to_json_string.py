#!/usr/bin/python3
"""A function that returns the JSON represerntation of a string."""
import json


def to_json_string(my_obj):
    """returns json rep of obj"""
    return json.dumps(my_obj)
