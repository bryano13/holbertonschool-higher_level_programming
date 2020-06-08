#!/usr/bin/python3
"""Module that writes text into a file"""


def write_file(filename="", text=""):
    """function that returns the len of text"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
