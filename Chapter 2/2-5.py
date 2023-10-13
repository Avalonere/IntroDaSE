def square_root(c, precision):
    approx = c / 2
    count = 0
    if approx:
        while abs(approx**2 - c) > precision:
            approx = (approx + c / approx) / 2
            count += 1
    return approx, count


print(square_root(2000, 0.00001))
