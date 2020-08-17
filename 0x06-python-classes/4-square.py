#!/bin/bash
a = [11, 3, 8, 5, 22]
b = [6, 7, 11, 22, 27]

set1 = set(a) - set(b)
set2 = set(b) - set(a)
list1 = list(set1) + list(set2)
result = set(a + b) - set(list1)

output = set(a) - (set(a) - set(b))

print(set1)
print(set2)
print(list1)
print(list(output))
