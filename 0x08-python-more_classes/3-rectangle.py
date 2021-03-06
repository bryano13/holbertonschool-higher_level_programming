#!/usr/bin/python3
""" This documents declares the class rectangle """


class Rectangle ():
    """ This class is the rectangle definition """
    def __init__(self, width=0, height=0):
        """Creates an instance for the class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        final_message = ""
        if (self.__width == 0 or self.__height == 0):
            return final_message
        for i in range(self.__height):
            for j in range(self.__width):
                final_message += '#'
            if (i != self.__height - 1):
                final_message += '\n'
        return final_message
