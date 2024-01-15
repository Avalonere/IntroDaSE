def cube_root(number, precision):
    digits = len(str(precision).split(".")[-1])
    if number < 0:
        low = number
        high = 0
    else:
        low = 0
        high = number
    mid = (low + high) / 2
    while abs(mid**3 - number) > precision:
        if mid**3 < number:
            low = mid
        if mid**3 > number:
            high = mid
        mid = (low + high) / 2
    return round(mid, digits)
