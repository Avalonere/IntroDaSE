import math


def int_dec2bin(n):
    num = ""
    while n > 0:
        num += str(n % 2)
        n //= 2
    return eval(num[::-1])


def frac_dec2bin(x, precision):
    num = ""
    while (x > 0) & (len(num) <= precision):
        if x * 2 >= 1:
            num += "1"
            x = x * 2 - 1
        else:
            num += "0"
            x *= 2
    return eval(num)


def dec2bin(x, precision):
    temp = abs(x)
    int = int_dec2bin(math.floor(temp))
    frac = frac_dec2bin(temp - math.floor(temp), precision)
    if x < 0:
        print("-", end="")
    print(int, ".", frac, sep="")
