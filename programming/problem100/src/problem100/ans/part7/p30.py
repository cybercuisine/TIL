from collections import deque

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
INF = 10 ** 10

H, W, N = map(int, input().split())
factory = [input() for _ in range(H)]

sx = 0
sy = 0
goals = {}
for i in range(H):
    for j in range(W):
        p = factory[i][j]
        if p == "S":
            goals[0] = tuple((i, j))
        elif p == "X" or p == ".":
            continue
        else:
            goals[int(p)] = tuple((i, j))

def bfs(start, goal):
    queue = deque([start])
    cost = [[INF] * W for _ in range(H)]
    sx = start[0]
    sy = start[1]
    cost[sx][sy] = 0
    for d in delta:
        qx = d[0] + start[0]
        qy = d[1] + start[1]
        if 0 <= qx < H and 0 <= qy < W:
            queue.append(tuple((qx, qy)))
    while len(queue) > 0:
        q = queue.popleft()
        qx = q[0]
        qy = q[1]
        if factory[qx][qy] == "X":
            continue

        for d in delta:
            nx = qx + d[0]
            ny = qy + d[1]
            if 0 <= nx < H and 0 <= ny < W:
                if cost[nx][ny] > cost[qx][qy] + 1:
                    cost[nx][ny] = cost[qx][qy] + 1
                    queue.append(tuple((nx, ny)))

    gx, gy = goal[0], goal[1]
    return cost[gx][gy]

ans = 0
for i in range(N):
    ans += bfs(goals[i], goals[i + 1])

print(ans)