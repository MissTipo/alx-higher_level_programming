#!/usr/bin/python3
"""
A class that inherits from the class list
"""


class MyList(list):
    """Derived class"""
    def __init__(self):
        """initializes the attributes of MyList class"""
        super().__init__()


    def print_sorted(self):
        """Prints sorted list in ascending order"""
        print(sorted(self))
