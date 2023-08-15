#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    sum1 = len(tuple_a)
    sum2 = len(tuple_b)

    total = ((tuple_a[0] if sum1 > 0 else 0) + (tuple_b[0] if sum2 > 0 else 0),
             (tuple_a[1] if sum1 > 1 else 0) + (tuple_b[1] if sum2 > 1 else 0))

    return total
