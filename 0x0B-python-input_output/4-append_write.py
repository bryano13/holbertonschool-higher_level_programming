#!/usr/bin/python3
"""Module that appends text to a file"""


def append_write(filename="", text=""):
    """Function that returns len of text appended"""

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
