#!/usr/bin/python3
"""This module returns the number of lines of a textfile"""


def read_lines(filename="", nb_lines=0):
    """funcion that return number of lines"""

    with open(filename, encoding="utf-8") as file:
        count = 0
        for line in file:
            print(line, end="")
            count += 1
            if count == nb_lines:
                break
