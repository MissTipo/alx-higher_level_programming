#!/usr/bin/python3
"""
This is a module to add two numbers

This module performs addition operation between two integers,
or two floats and raises an exception if the number is not an 
integer or a float.

"""


def add_integer(a, b=98):
    """Adds two numbers

    Return the addition of two numbers with spcific validation.

    Arguments:
        a (int or float): first value to add
        b (int or float): second value to add
    Return:
        the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b

def convert_to_int(num):
    """Casts the data type of the num parameter

    Converts a float number to an integer

    Arguments:
        num(int or float): the number to cast.

    Returns:
        int: The number casted to integer

    """
    if type(num) is float:
        num = int(num)
        return num

    return num
