#!/usr/bin/python3
"""Class Rectangle that inherits from class Base"""

from models.base import Base


class Rectangle(Base):
    """Class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and setter for width
    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    # --------------------------------------------------

    # Getter and setter for height
    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    # ------------------------------------------------------

    # Getter and Setter for x
    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    # --------------------------------------------------------

    # Getter and Setter for y
    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    # ---------------------------------------------------------

    # area method
    def area(self):
        """Method that calculates the area of Rectangle"""
        return self.__width * self.__height

    # display method
    def display(self):
        """Method that displays the rectangle in hashtags #"""

        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    # __str__ method
    def __str__(self):
        """Overrides str default str method"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        ar = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, ar[i], args[i])
        if kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a rectange"""
        # It has to return a new dictionary
        dict1 = {"x": self.x, "y": self.y, "id": (
            self.id), "height": self.height, "width": self.width}
        return dict1
