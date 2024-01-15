# 时间复杂度 最好情况O(n**1.3)，最差情况O(n**2);空间复杂度O(1)


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
