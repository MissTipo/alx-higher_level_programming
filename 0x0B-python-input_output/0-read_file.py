#!/usr/bin/python3
"""
Contains a function that reads a text file
"""


def read_file(filename=""):
    """reads a text file and prints it out"""
    with open("UTF8", "r", encoding=("utf-8")) as f:
        print(f.read(), end='')
