#!/usr/bin/python3
"""
Contains a derived class Square that inherits
from the base class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from the class Rectangle"""
    def __init__(self, size):
        """Instantiates the attributes of class Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of class square"""
        return self.__size ** 2
