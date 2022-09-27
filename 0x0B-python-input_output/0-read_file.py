#!/usr/bin/python3
"""
Contains a function that reads a text file
"""


def read_file(filename=""):
    """read a text file(UTF8) and prints it"""
    with open(filename, "r", encoding=("utf8")) as text:
        print(text.read(), end="")
