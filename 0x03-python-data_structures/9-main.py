#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90.3, 2, 13, 90.3, 5, -13, 3, 20, 90.1, 90.2]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
