def split(n):
    if n <= 4:
        return [n]
    if n % 2 == 0:
        half = n // 2
        return split(half) + split(half)
    else:
        half1 = (n - 1) // 2
        half2 = (n + 1) // 2
        return split(half1) + split(half2)
