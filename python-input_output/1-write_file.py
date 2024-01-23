#!/usr/bin/python3
""" A function that writes a string to a UTF-8 text file and returns
    the number of characters written.
"""


def write_file(filename="", text=""):
    """writes to text file and returns # of chars printed"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
