# x(n+1) = (2 * x(n) + c / x(n)**2) / 3
def cube_root(c, precision):
    approx = c / 2
    count = 0
    if approx:
        while abs(approx**3 - c) > precision:
            approx = (2 * approx + c / approx**2) / 3
            count += 1
    return approx, count


print(cube_root(10, 0.00001))
