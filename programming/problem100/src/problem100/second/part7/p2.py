from collections import deque

R, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
C = [list(input()) for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

ans = 0
que = deque([[sy, sx]])
delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]
dist = [[float('inf')] * W for _ in range(R)]
dist[sy][sx] = 0
while que:
    y, x = que.pop()
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < W and 0 <= ny < R:
            if dist[ny][nx] > dist[y][x] + 1 and C[y][x] != "#":
                dist[ny][nx] = dist[y][x] + 1
                que.append([ny, nx])

print(dist[gy][gx])