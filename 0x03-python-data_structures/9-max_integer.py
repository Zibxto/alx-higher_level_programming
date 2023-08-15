#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        i = 0
        length = len(my_list)
        for x in my_list:
            while x >= my_list[i]:
                i += 1
                if i == length - 1:
                    return x
