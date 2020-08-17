#!/usr/bin/python3
"""Module that contans the class Base"""
import json


class Base():
    """Parent class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance attributes"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Static method--------------------------------

    @staticmethod
    def to_json_string(list_dictionaries):
        dict_str = json.dumps(list_dictionaries)
        return dict_str

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        dict_list = []
        with open(filename, "w") as my_file:
            if list_objs:
                for i in list_objs:
                    dict_list.append(i.to_dictionary())
            my_file.write(Base.to_json_string(dict_list))

    # from json string method--------------------------------

    @staticmethod
    def from_json_string(json_string):
        dict_list = []
        if json_string:
            dict_list = json.loads(json_string)
        return dict_list

    # create method-------------------------------------------
    @classmethod
    def create(cls, **dictionary):

        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)

        elif cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):

        filename = cls.__name__ + ".json"
        with open(filename) as my_file:
            json_str = my_file.read()
            dict_list = cls.from_json_string(json_str)
            obj_list = []
            for dictionary in dict_list:
                obj_list.append(cls.create(**dictionary))
            return obj_list
