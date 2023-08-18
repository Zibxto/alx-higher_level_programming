#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        mul = 1
        total = 0
        weight = 0
        for x in my_list:
            for y in x:
                mul *= y
            total += mul
            mul = 1
            weight += y
        result = total / weight
        return (result) if result > 0 else 0
    else:
        return 0
