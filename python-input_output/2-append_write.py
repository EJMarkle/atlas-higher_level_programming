#!/usr/bin/python3
""" A function that appends a string to the end of a UTF-8 text file,
    and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """appends string to file, returns chars added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
