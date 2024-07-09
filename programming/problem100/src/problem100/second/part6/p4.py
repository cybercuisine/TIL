import sys

sys.setrecursionlimit(10**7)

n = int(input())
m = int(input())
ices = [list(map(int, input().split())) for _ in range(m)]


def dfs(i: int, j: int, length: int):
    global ans
    if ices[i][j] == 0:
        return
    ans = max(ans, length)
    ices[i][j] = 0
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for dx, dy in d:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < m and 0 <= ny < n:
            dfs(nx, ny, length + 1)
    ices[i][j] = 1


ans = 0
for j in range(n):
    for i in range(m):
        if ices[i][j] == 0:
            continue
        length = 1
        dfs(i, j, length)

print(ans)
