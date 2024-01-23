#!/usr/bin/python3
"""A function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """creates obj from json"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
