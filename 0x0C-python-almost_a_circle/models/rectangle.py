#!/usr/bin/python3
"""Subclass Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Subclass Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # width getter:
    @property
    def width(self):
        return self.__width

    # width setter:
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height---------------------------------------------
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x ---------------------------------------------------
    @property
    def x(self):
        return self.__x

    # x setter:
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y getter
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    # Area Method---------------------------------------------

    def area(self):
        return self.width * self.height

    # Display method------------------------------------------

    def display(self):
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    # str method------------------------------------------------

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    # update method----------------------------------------------

    def update(self, *args, **kwargs):
        ar_list = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, ar_list[i], args[i])
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    # Dictionary method-------------------------------------

    def to_dictionary(self):
        new_dict = {"id": self.id, "width": self.width, "height": (
            self.height), "x": self.x, "y": self.y}
        return new_dict
