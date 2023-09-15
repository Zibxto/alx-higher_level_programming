#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains function that creates an object from a json file
"""


def load_from_json_file(filename):
    """
    Creates an object from a json file

    Args:
        filename(str): name of file
    """

    import json

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
