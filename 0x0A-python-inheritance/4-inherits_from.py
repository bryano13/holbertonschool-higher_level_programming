#!/usr/bin/python3
""" module for inherit_form"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class
    that inherited (directly or indirectly) """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
