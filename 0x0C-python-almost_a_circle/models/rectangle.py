#!/usr/bin/python3
"""This module containes a derived class"""


class Rectangle(Base):

    """a derived class that inerits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """Instance method"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__(id)
