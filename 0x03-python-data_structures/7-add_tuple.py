#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    if len1 < 2:
        if len1 == 0:
            val1 = 0
            val2 = 0
        elif len1 == 1:
            val1 = tuple_a[0]
            val2 = 0
    else:
        val1 = tuple_a[0]
        val2 = tuple_a[1]
    if len2 < 2:
        if len2 == 0:
            val3 = 0
            val4 = 0
        elif len2 == 1:
            val3 = tuple_b[0]
            val4 = 0
    else:
        val3 = tuple_b[0]
        val4 = tuple_b[1]
    add = val1 + val3
    add2 = val2 + val4
    new_tuple = add, add2,
    return new_tuple
