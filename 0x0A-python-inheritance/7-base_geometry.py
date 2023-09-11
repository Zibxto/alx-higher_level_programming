#!/usr/bin/python3
"""
Module 7-base_geometry
Contains a class BaseGeometry
"""


class BaseGeometry:
    """
    Contains 2 methods area and integer_validator
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a given value as an int or not

        Args:
            name(str): name of value parameter
            value(int): value to be validated
        """
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError(self.name + " must be an integer")
        if self.value <= 0:
            raise ValueError(self.name + " must be greater than 0")
