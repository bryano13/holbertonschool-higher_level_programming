#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            letter = chr(ord(str[i]) - 32)
        else:
            letter = chr(ord(str[i]))
        print("{}".format(letter), end="")
    print("")
