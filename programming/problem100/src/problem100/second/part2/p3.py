N = int(input())
area = {}
points = []

for i in range(N):
    x, y = map(int, input().split())
    if x not in area:
        area[x] = []
    area[x].append(y)
    points.append((x, y))

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]

        dx = x2 - x1
        dy = y2 - y1

        if x1 + dy in area and x2 + dy in area:
            if y1 - dx in area[x1 + dy] and y2 - dx in area[x2 + dy]:
                ans = max(ans, dx**2 + dy**2)

        if x1 - dy not in area or x2 - dy not in area:
            continue

        if y1 + dx in area[x1 - dy] and y2 + dx in area[x2 - dy]:
            ans = max(ans, dx**2 + dy**2)

print(ans)
