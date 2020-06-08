#!/usr/bin/python3
""" module for is_same_class"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of the specified"""
    if type(obj) is a_class:
        return True
    else:
        return False