#!/usr/bin/python3
"""
Returns True if the object is an instance of
a class that inherited directly or indirectly
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of subclass
    Arguments:
    obj: The object to check
    a_class: The class to match the obj to
    Returns:
    True if is instance, otherwise false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
