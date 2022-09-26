#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with a function that raises exception"""
    def area(self):
        """a public instance method that raises an exception"""
        raise Exception("area() is not implemented")
