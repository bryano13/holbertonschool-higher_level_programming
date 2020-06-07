#!/usr/bin/python3
"""This module defines the class Rectange"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that builds a rectangle"""

    def __init__(self, width, height):
        """
        Initializes instance of the rectangle

        Args:
            width: width for __width atribute
            height: height for the __height attribute
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns area of instance"""
        
        return self.__width * self.__height

    def __str__(self):
        """returns string representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
