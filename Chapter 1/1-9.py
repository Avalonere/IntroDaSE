def reverse_1(ls):
    length = len(ls)
    flag = length % 2
    for i in range(0, int((length - flag) / 2)):
        ls[i], ls[length - 1 - i] = ls[length - 1 - i], ls[i]
    return ls


def reverse_2(ls):
    length = len(ls)
    flag = length % 2
    i = 0
    while i <= int((length - flag) / 2):
        ls[i], ls[length - 1 - i] = ls[length - 1 - i], ls[i]
        i += 1
    return ls
