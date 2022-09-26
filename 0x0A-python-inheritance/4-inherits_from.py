#!/usr/bin/python3
"""
Returns True if the object is an instance of a subclass
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
