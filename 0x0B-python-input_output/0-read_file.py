#!/usr/bin/python3
"""This module reads a text file"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout
    Args:
        filename (str): Filename
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
