#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = [0, 0]
    d = [0, 0]
    if tuple_a:
        c[0] = tuple_a[0]
        if len(tuple_a) >= 2:
            c[1] = tuple_a[1]
    if tuple_b:
        d[0] = tuple_b[0]
        if len(tuple_b) >= 2:
            d[1] = tuple_b[1]
    sum = c[0] + d[0], c[1] + d[1]
    return sum
