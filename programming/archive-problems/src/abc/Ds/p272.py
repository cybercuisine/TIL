from collections import deque

N, M = map(int, input().split())

d = []
for a in range(-10**3 - 10, 10**3 + 10):
    for b in range(-10**3 - 10, 10**3 + 10):
        if a**2 + b**2 == M:
            d.append([a, b])

Grid = [[-1] * (N + 1) for _ in range(N + 1)]
Grid[1][1] = 0

que = deque()
que.append([1, 1])

while que:
    NowG, NowR = que.popleft()
    Num = Grid[NowG][NowR]

    for Gd, Rd in d:
        if 1 <= NowG + Gd <= N and 1 <= NowR + Rd <= N:
            if Grid[NowG + Gd][NowR + Rd] == -1:
                Grid[NowG + Gd][NowR + Rd] = Num + 1
                que.append([NowG + Gd, NowR + Rd])

for G in range(1, N + 1):
    print(*Grid[G][1:])
