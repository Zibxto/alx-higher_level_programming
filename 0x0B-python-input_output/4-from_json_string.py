#!/usr/bin/python3
"""
Module 4-from_json_string
Contains function that returns an object
(python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """
    Returns the object representation of a json string

    Args:
        my_str(str): string
    """

    import json

    return json.loads(my_str)
