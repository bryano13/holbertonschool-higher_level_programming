#!/usr/bin/python3
"""File that creates a class Rectangle"""


class Rectangle:
    """Creating a class Rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        string = ""
        if self.height == 0 or self.width == 0:
            return string
        else:
            for i in range(0, self.height):
                for j in range(0, self.width):
                    string = string + "#"
                if i < self.height -1:
                    string = string + "\n"
            return string

    def __repr__(self):
        """Returns a string for developer"""
        output = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return output

    def __del__(self):
        """When an instance is deleted print a message"""
        print("Bye Rectangle...")
