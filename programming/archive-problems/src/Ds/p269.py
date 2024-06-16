OFFSET = 1000
MAX_INDEX  = OFFSET * 2 + 1

f = [[0 for j in range(MAX_INDEX)] for i in range(MAX_INDEX)]
diff_x = [-1, -1, 0, 0, 1, 1]
diff_y = [-1, 0, -1, 1, 0, 1]


def dfs(x, y):
    f[x][y] = 0
    for i in range(6):
        if 0 <= diff_x[i] + x and diff_x[i] + x < MAX_INDEX and \
           0 <= diff_y[i] + y and diff_y[i] + y < MAX_INDEX and \
           f[diff_x[i] + x][diff_y[i] + y] == 1:
            dfs(diff_x[i] + x, diff_y[i] + y)


n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    f[x + OFFSET][y + OFFSET] = 1

result = 0
for x in range(MAX_INDEX):
    for y in range(MAX_INDEX):
        if f[x][y] == 1:
            result += 1
            dfs(x, y)

print(result)