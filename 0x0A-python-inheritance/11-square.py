#!/usr/bin/python3
"""This module defines the class square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creating a class Square"""


    def __init__(self, size):
        """Initializes instance of square"""

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns string Representation"""

        return "[Square] {}/{}".format(self.__size, self.__size)
