import math
import random


def pi_approx_leibniz(n):
    total = 0
    for i in range(1, n + 1):
        total += (-1) ** (i + 1) / (2 * i - 1)
    pi = total * 4
    return pi


def pi_approx_monte_carlo(n):
    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            count += 1
    pi = count / n * 4
    return pi


def pi_approx_cyclotomy(n):
    polygon = 6
    radius = 100
    s = radius
    for i in range(n):
        a = s / 2
        b = math.sqrt(radius**2 - a**2)
        c = radius - b
        s = math.sqrt(a**2 + c**2)
        polygon *= 2
    perimeter = polygon * s
    pi = perimeter / (radius * 2)
    return pi
