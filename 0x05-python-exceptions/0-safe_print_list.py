#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for index, element in enumerate(my_list):
            if index < x:
                print(element, end="")
                i += 1
        print()
        return (i)
        i = 1
    except IndexError:
        print("Index is out of range")
