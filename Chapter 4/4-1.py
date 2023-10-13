def is_prime(x):
    flag = 1
    for i in range(2, x):
        if x % i == 0:
            flag = 0
            break
    if x == 1:
        flag = 0
    return flag
