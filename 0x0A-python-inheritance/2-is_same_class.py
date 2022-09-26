#!/usr/bin/python3
"""
Returns True if the object is exactly an instace
of the specified class, otherwise False
"""

def is_same_class(obj, a_class):
    """Returns true if an object in instance of a class"""
    return type(obj) == a_class
