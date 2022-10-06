#!/usr/bin/python3
"""This module containes a derived class"""


class Rectangle(Base):

    """a derived class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """Instantiates the class Rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, parameter):
        """width setter"""
        self.__width = parameter

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, parameter):
        """height setter"""
        self.__height = parameter

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, parameter):
        """x setter"""
        self.__x = parameter

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, parameter):
        """y setter"""
        self.__y = parameter
