from collections import deque

INF = 10 ** 10

answers = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    cost = [[INF] * w for _ in range(h)]
    cost[0][0] = 1
    yoko = []
    tate = []
    for i in range(2 * h - 1):
        wall = list(map(int, input().split()))
        if i % 2 == 0:
            yoko.append(wall)
        else:
            tate.append(wall)
    
    q = deque([[0, 0]])

    while len(q) > 0:
        point = q.popleft()
        x, y = point[1], point[0]

        if x + 1 < w and yoko[y][x] == 0 and cost[y][x + 1] > cost[y][x] + 1:
            cost[y][x + 1] = cost[y][x] + 1
            q.append([y, x + 1])
        if x - 1 >= 0 and yoko[y][x - 1] == 0 and cost[y][x - 1] > cost[y][x] + 1:
            cost[y][x - 1] = cost[y][x] + 1
            q.append([y, x - 1])
        if y + 1 < h and tate[y][x] == 0 and cost[y + 1][x] > cost[y][x] + 1:
            cost[y + 1][x] = cost[y][x] + 1
            q.append([y + 1, x])
        if y - 1 >= 0 and tate[y - 1][x] == 0 and cost[y - 1][x] > cost[y][x] + 1:
            cost[y - 1][x] = cost[y][x] + 1
            q.append([y - 1, x])
    
    answers.append(cost[h - 1][w - 1])
    
for ans in answers:
    if ans == INF:
        print(0)
    else:
        print(ans)
