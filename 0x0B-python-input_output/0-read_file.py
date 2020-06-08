#!/usr/bin/python
"""This module reads a text file"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    Args:
        filename (str): Filename
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
