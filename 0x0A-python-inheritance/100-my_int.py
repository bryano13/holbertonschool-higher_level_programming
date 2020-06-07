#!/usr/bin/python3
"""Subclass MyInt inverts __eq__ and __ne__ methods"""


class MyInt(int):
    """Method that changes == to != and viceversa"""

    def __eq__(self, value):
        return bool.__ne__(self, value)

    def __ne__(self, value):
        return bool.__eq__(self, value)
