#!/usr/bin/python3
"""
Module 5-save_to_json_file
Contains function that writes an object to a text file,
using a json representaion
"""


def save_to_json_file(my_obj, filename):
    """
    Returns the object representation of a json string

    Args:
        my_obj(dict): object
        filename(str): name of file
    """

    import json

    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
