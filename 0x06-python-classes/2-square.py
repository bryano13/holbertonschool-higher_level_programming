#!/usr/bin/python3
#def window(size):
size = 3
ar = [2, 3, 4, 2, 6, 2, 5, 1]

for index in range(0, len(ar)):
    val = index
    if val >= index and val <= index + size:
        max(ar[index], ar[index + size])

