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
