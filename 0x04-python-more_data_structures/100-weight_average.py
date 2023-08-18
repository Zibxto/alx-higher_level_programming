#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total = 0
        frequency = 0
        for tup in my_list:
            (weight, occurrence) = tup
            total += weight * occurrence
            frequency += occurrence
        result = total / frequency if frequency > 0 else 0
        return result
    else:
        return 0
