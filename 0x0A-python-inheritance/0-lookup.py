#!/usr/bin/python3
"""
returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Returns all attributes and methods of an object"""
    fun = dir(obj)
    return fun
