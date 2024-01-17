def square_root(c, precision, step):
    g, j, i = 0, 0, 0
    while j**2 < c:
        j += 1
    g = j - 1
    while abs(g**2 - c) > precision:
        g += step
        i += 1
    return g, i
