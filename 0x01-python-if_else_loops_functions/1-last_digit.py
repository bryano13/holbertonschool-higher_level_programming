#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    ldigit = (((number * -1) % 10) * -1)
else:
    ldigit = number % 10

print("Last digit of {0:d} is {1:d} and is".format(number, ldigit), end=" ")
if ldigit > 5:
    print("greater than 5")
elif ldigit < 6 and ldigit is not 0:
    print("less than 6 and not 0")
elif ldigit == 0:
    print("0")
