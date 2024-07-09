answers = []

delta = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    C = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    def dfs(x, y):
        visited[x][y] = True
        if C[x][y] == 0:
            return 0
        for dx, dy in delta:
            if 0 <= x + dx < h and 0 <= y + dy < w:
                if not visited[x + dx][y + dy]:
                    dfs(x + dx, y + dy)
        return 1

    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                ans += dfs(i, j)
    
    answers.append(ans)


print(*answers, sep="\n")
