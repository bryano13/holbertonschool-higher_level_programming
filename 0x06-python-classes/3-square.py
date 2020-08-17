#!/usr/bin/python3
"""File that creates a class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Creation of instances private attribute size"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
