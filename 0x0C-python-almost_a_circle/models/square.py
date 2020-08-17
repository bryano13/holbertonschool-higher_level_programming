#!/usr/bin/python3
"""subclass Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Subclass Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    # Getters and setters--------------------------------
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    # Update method--------------------------------------

    def update(self, *args, **kwargs):
        arg_list = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, arg_list[i], args[i])
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    # Dictionary method----------------------------------------

    def to_dictionary(self):
        new_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return new_dict
