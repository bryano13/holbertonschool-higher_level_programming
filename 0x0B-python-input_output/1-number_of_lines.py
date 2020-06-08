#!/usr/bin/python3
"""This module returns the number of lines of a textfile"""


def number_of_lines(filename=""):
    """funcion that return number of lines"""

    with open(filename, encoding="utf-8") as file:
        count = 0
        for line in file:
            count += 1
        return count
