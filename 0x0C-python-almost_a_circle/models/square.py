#!/usr/bin/python3
"""Subclass Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Subclass Square creation"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of attributes"""
        self.size = size
        super().__init__(size, size, x, y, id)

    # size getter
    @property
    def size(self):
        return self.width

    # size setter
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.width = value
        self.height = value

    # str method
    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Update class variables """
        ar = ["id", "size", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, ar[i], args[i])
        if args:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """sends instance rep in dict format"""
        new_dict = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
        return new_dict
