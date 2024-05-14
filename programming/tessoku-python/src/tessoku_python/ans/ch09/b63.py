H, W = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

S = [input() for i in range(H)]

INF = 1 << 61
cost = [[INF] * W for i in range(H)]

q = []
def push(x: int, y: int, c: int):
    if S[x][y] == '#':
        return
    if cost[x][y] <= c:
        return
    cost[x][y] = c
    q.append((x, y))

push(sx, sy, 0)

for x,y in q:
    c2 = cost[x][y] + 1
    push(x - 1, y, c2)
    push(x, y - 1, c2)
    push(x + 1, y, c2)
    push(x, y + 1, c2)

print(cost[gx][gy])
