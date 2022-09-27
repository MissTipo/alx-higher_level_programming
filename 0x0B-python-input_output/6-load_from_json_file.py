#!/usr/bin/python3
"""
Contains a function that creates an Object from a “JSON file”
"""


from json import loads


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding='utf-8') as f:
        return loads(f.read())
