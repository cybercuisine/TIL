from collections import deque

INF = 10 ** 10
delta = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

maze = [input() for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

def bfs(start_x: int, start_y: int):
    cnt = [[INF] * C for _ in range(R)]
    cnt[start_y][start_x] = 0
    points = deque([])
    for d in delta:
        if 0 <= start_x + d[0] < C and 0 <= start_y + d[1]:
            points.append([start_x + d[0], start_y + d[1]])
    while len(points) > 0:
        p = points.pop()
        px = p[0]
        py = p[1]
        if maze[py][px] == "#":
            continue
        for d in delta:
            nx = px + d[0]
            ny = py + d[1]
            if 0 <= nx < C and 0 <= ny < R:
                if cnt[ny][nx] > cnt[py][px] + 1:
                    cnt[ny][nx] = cnt[py][px] + 1
                    points.append([nx, ny])
    return cnt

cnt = bfs(sx, sy)

if cnt[gy][gx] == INF:
    print(-1)
else:
    print(cnt[gy][gx])