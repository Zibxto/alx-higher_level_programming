#!/usr/bin/python3
import json
"""
Module 3-to_json_string
Contains function that returns the json representation of an object
"""


def to_json_string(my_obj):
    """
    Returns the json representation of a string

    Args:
        my_obj(dict): object
    """
    return json.dumps(my_obj)
