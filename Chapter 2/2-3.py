# 用列表存储答案序列
answer = []
# 用字典存储过程描述
description = {0: "人和狼过河了", 1: "人和羊过河了", 2: "人和菜过河了", 3: "人自己过河了"}
# 用列表推导式创建一个长度为 16 的布尔值列表，表示是否已经遍历过某个状态，初始都没有遍历
visited = [False for _ in range(16)]
# 标记初始状态为已遍历
visited[0] = True


# 定义一个函数，根据四个变量的值，返回一个整数表示状态
def get_state(a, b, c, d):
    return a << 3 | b << 2 | c << 1 | d


# 定义一个深度优先搜索的函数，参数是当前状态
def dfs(current):
    # 如果当前状态是 15，即所有生物都过河了，输出答案序列并返回
    if current == 15:
        print(" ".join(answer))
        return
    # 根据当前状态的二进制表示，获得所有生物的状态
    person, wolf, sheep, cabbage = ((current >> i) & 1 for i in range(3, -1, -1))
    # 将所有生物的状态和人放入一个元组
    state = (person, wolf, sheep, cabbage, person)
    # 如果人不在时，狼和羊在一起，或者羊和白菜在一起是无效状态，直接返回
    if person != sheep and (sheep == cabbage or wolf == sheep):
        return
    # 定义一个元组，存储四种可能的转移后的状态，分别对应人和狼、人和羊、人和菜、人自己过河
    next_states = (
        get_state(1 - person, 1 - person, sheep, cabbage),
        get_state(1 - person, wolf, 1 - sheep, cabbage),
        get_state(1 - person, wolf, sheep, 1 - cabbage),
        get_state(1 - person, wolf, sheep, cabbage),
    )
    # 遍历所有生物（除了人）
    for i, j in enumerate(state[1:]):
        # 如果人和该生物在一边，并且转移后的状态没有被遍历过
        if person == j and (not visited[next_states[i]]):
            # 标记转移后的状态为已遍历
            visited[next_states[i]] = True
            # 将对应的过程描述加入答案序列
            answer.append(description[i])
            # 继续搜索转移后的状态
            dfs(next_states[i])
            # 回溯时，将之前加入的过程描述移除答案序列
            answer.pop()
            # 标记转移后的状态为未遍历
            visited[next_states[i]] = False


# 从初始状态开始搜索
dfs(0)
