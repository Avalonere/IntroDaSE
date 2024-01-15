import math
import random


def integral_approx(n):
    count = 0
    for i in range(n):
        x = random.uniform(2, 3)
        y = random.uniform(0, 21)
        if y <= x**2 + 4 * x * math.sin(x):
            count += 1
    integral = count / n * 21
    return integral
