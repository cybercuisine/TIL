N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
points_set = set(XY)
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        if x1 != x2 and y1 != y2:
            if (x1, y2) in points_set and (x2, y1) in points_set:
                ans += 1

print(ans // 2)
