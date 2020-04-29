#!/str/bin/python3
def print_last_digit(number):   
    number = abs(number)
    if (number/10) > 0 and (number/10) < 1:
        digit = number
    else:
        digit = number % 10
    print("{:d}".format(digit), end="")
    return digit
