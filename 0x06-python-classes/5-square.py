#!/usr/bin/python3
"""File that creates a class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Creation of instances private attribute size"""
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """Method to retreive size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setting a new value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value
    
    def my_print(self):
        """Prints the area using # hashtags elements"""
        if self.__size > 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
