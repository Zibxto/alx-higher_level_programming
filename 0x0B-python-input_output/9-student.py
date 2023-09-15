#!/usr/bin/python3
"""
Module 9-student.py
Contains a class Student
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Public instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrives a dictionary representaion of a stident instance
        """
        return self.__dict__
