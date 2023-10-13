def a2b(a):
    b = []
    for i in range(len(a)):
        prod = 1
        for j in range(len(a)):
            if j != i:
                prod *= a[j]
        b.append(prod)
    return b
