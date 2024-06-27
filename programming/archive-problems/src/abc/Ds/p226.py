import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

S = set()

for i in range(N):
    x1, y1 = XY[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2 = XY[j]
        g = math.gcd(x1 - x2, y1 - y2)
        x = (x1 - x2) // g
        y = (y1 - y2) // g
        S.add((x, y))

print(len(S))