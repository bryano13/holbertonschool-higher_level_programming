#!/usr/bin/python
"""Module that saves object to a Json File"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text
    file, using a JSON representation
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
