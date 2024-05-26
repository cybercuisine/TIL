from collections import deque

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
INF = 10 ** 10

H, W = map(int, input().split())
S = [input() for _ in range(H)]

black_init = 0
for s in S:
    black_init += s.count("#")

cost = [[INF] * W for _ in range(H)]
cost[0][0] = 0
q = deque([[0, 0]])

while len(q) > 0:
    point = q.popleft()
    x, y = point[0], point[1]
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < W and 0 <= ny < H:
            if S[ny][nx] == "#":
                continue
            if cost[ny][nx] > cost[y][x] + 1:
                cost[ny][nx] = cost[y][x] + 1
                q.append([nx, ny])


if cost[H - 1][W - 1] == INF:
    print(-1)
else:
    print(H*W - black_init - cost[H - 1][W - 1] - 1)