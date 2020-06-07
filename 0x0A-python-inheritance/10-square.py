#!/usr/bin/python3
"""Class Square that inherits from class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creation of class Square"""

    def __init__(self, size):
        """Initizalization of the instance attributes"""

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
