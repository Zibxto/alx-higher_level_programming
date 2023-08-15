#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        biggest_int = my_list[0]
        for x in my_list:
            if x > biggest_int:
                biggest_int = x
        return biggest_int
    else:
        return None
