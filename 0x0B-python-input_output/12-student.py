#!/usr/bin/python3
"""Module Class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        new_dict = {}
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for att in attrs:
                if att in self.__dict__:
                    new_dict[att] = self.__dict__[att]
            return new_dict
        return self.__dict__
