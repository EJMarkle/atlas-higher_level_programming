#!/usr/bin/python3
"""A function that reads a UTF-8 text file and prints it to stdout."""


def read_file(filename=""):
    """reads and prints the file"""
    with open(filename, "r", encoding="utf=8") as file:
        print(file.read(), end= "")
