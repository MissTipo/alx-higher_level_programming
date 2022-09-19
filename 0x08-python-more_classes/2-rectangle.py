#!/usr/bin/python3
"""
a module that defines a Rectangle Class
"""


class Rectangle:
    """Represents an empty class Rectangle"""
    def __init__(self, width=0, height=0):
        """checks parameters and initializes the attribute values"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Checks parameters and sets the width of the Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of thhe Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Checks parameters and sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a square"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeters of a square"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)
