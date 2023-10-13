import random
import time


def rad_list(n):
    ls = []
    for i in range(n):
        ls.append(random.randint(1, 100))
    return ls


def bubble_sort(ls):
    n = len(ls)
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls


def selection_sort(ls):
    n = len(ls)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if ls[j] < ls[min_index]:
                min_index = j
        if i != min_index:
            ls[i], ls[min_index] = ls[min_index], ls[i]
    return ls


def straight_insertion_sort(ls):
    n = len(ls)
    for i in range(1, n):
        current = ls[i]
        pre_index = i - 1
        while pre_index >= 0 and current < ls[pre_index]:
            ls[pre_index + 1] = ls[pre_index]
            pre_index -= 1
        ls[pre_index + 1] = current
    return ls


def shell_sort(ls):
    n = len(ls)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            current = ls[i]
            pre_index = i - gap
            while pre_index >= 0 and current < ls[pre_index]:
                ls[pre_index + gap] = ls[pre_index]
                pre_index -= gap
            ls[pre_index + gap] = current
        gap = gap // 2
    return ls


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


def merge_sort(ls):
    n = len(ls)
    if n == 1:
        return ls
    middle = n // 2
    left = ls[:middle]
    right = ls[middle:]
    return merge(merge_sort(left), merge_sort(right))


def perf_analysis(sort, n):
    start = time.perf_counter()
    sort(rad_list(n))
    end = time.perf_counter()
    return end - start


# O(n^2)中，效率由高到低是插入，选择，冒泡
# O(nlogn)中，归并排序比希尔排序更高效
