import math
import random
import time

pi_10 = 3.1415926535
pi_10_upper = 3.1415926536


def pi_approx_monte_carlo(n):
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            count += 1
    pi = count / n * 4
    return pi


def pi_approx_leibniz():
    total = 0
    i = 1
    pi = 0
    while pi < pi_10 or pi >= pi_10_upper:
        total += (-1) ** (i + 1) / (2 * i - 1)
        pi = total * 4
        i += 1
    return pi


def pi_approx_cyclotomy():
    polygon = 6
    radius = 100
    s = radius
    i = 0
    pi = 0
    while pi < pi_10 or pi >= pi_10_upper:
        a = s / 2
        b = math.sqrt(radius**2 - a**2)
        c = radius - b
        s = math.sqrt(a**2 + c**2)
        polygon *= 2
        perimeter = polygon * s
        pi = perimeter / (radius * 2)
        i += 1
    return pi


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def pi_approx_ramanujan():
    total = 0
    i = 0
    pi = 0
    while pi < pi_10 or pi >= pi_10_upper:
        numerator = factorial(4 * i) * (1103 + 26390 * i)
        denominator = pow(factorial(i), 4) * pow(396, 4 * i)
        term = numerator / denominator
        total += term
        coefficient = 2 * math.sqrt(2) / 9801
        pi = 1 / (coefficient * total)
        i += 1
    return pi


def perf_analysis(pi_approx):
    start = time.perf_counter()
    pi_approx()
    end = time.perf_counter()
    return end - start


# 测试发现，Leibniz给出的公式虽然简单，但收敛非常慢，割圆术思想收敛相对快一些，而Ramanujan给出的公式收敛极快
