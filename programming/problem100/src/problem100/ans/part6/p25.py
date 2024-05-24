import sys
sys.setrecursionlimit(10 ** 7)

def dfs(y, x):
    c[y][x] = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            ny = y + dy
            nx = x + dx
            if 0 <= nx < w and 0 <= ny < h and c[ny][nx] == 1:
                dfs(ny, nx)
    return

ans = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    c = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == 1:
                dfs(i, j)
                cnt += 1
    ans.append(cnt)

for a in ans:
    print(a)