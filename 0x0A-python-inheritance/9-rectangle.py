#!/usr/bin/python3
"""
Contains a derived class
"""


class BaseGeometry:
    """a class with public method that raises exception"""
    def area(self):
        """a public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public instance method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """a derived class"""
    def __init__(self, width, height):
        """instantiates derived class attributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the class Rectangle"""
        return self.__width * self.__height
    def __str__(self):
        """returns description of the class Rectangle"""
        return "[Rectangle]{}/{}".format(self.__width, self.__height)
