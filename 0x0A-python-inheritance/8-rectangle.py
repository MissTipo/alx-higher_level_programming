#!/usr/bin/python3
"""
Contains a derived class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class inherits from the class baseGeometry"""
    def __init__(self, width, height):
        """a function that instantiates class attributes"""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
