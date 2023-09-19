#!/usr/bin/python3
"""
Module base
Contains a class called Base
"""


class Base:
    """This class represents a base class"""
    __nb_object = 0

    def __init__(self, id=None):
        """ Class constructor"""
        if id is not None:
            self.id = id
        else:
            __class__.__nb_object += 1
            self.id = __class__.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        import json
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
