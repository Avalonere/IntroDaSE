def is_valid_state(state):
    # 检查是否有不安全的状态，即狼吃羊或羊吃菜
    if (state[1] == state[2] and state[0] != state[1]) or (
        state[2] == state[3] and state[0] != state[2]
    ):
        return False
    return True


def dfs(state, path, visited):
    if state == (0, 0, 0, 0):
        # 找到了解决方案
        print("找到解决方案：", path)
        return

    for move in moves:
        new_state = tuple(state[i] + move[i] for i in range(4))
        if (
            all(0 <= new_state[i] <= 1 for i in range(4))
            and is_valid_state(new_state)
            and new_state not in visited
        ):
            visited.add(new_state)
            dfs(new_state, path + [new_state], visited)
            visited.remove(new_state)


# 初始状态：(1, 1, 1, 1) 表示人、狼、羊、菜都在起始岸
initial_state = (1, 1, 1, 1)
# 移动方式
moves = [
    (-1, 0, 0, 0),
    (-1, -1, 0, 0),
    (-1, 0, -1, 0),
    (-1, 0, 0, -1),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 1),
]

visited = set()
visited.add(initial_state)

dfs(initial_state, [initial_state], visited)
