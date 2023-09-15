#!/usr/bin/python3
"""
Module 6-add_item.py
Contains a script that adds all arguments to a python list,    
and then save them to a file
"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


json_file = "add_item.json"
args = sys.argv

try:
    my_list = load_from_json_file(json_file)
except FileNotFoundError:
    my_list = []

save_to_json_file(my_list + args[1:], json_file)
