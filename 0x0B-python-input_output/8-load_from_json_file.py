#!/usr/bin/python3
"""Module with function load_from_json_file"""
import json


def load_from_json_file(filename):
    """
    This funcion loads from a json file
    """

    with open(filename, encoding="utf-8") as file:
        return json.loads(file.read())
