import math

def distance(x1, y1, x2, y2) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

N, M = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
E = [list(map(int, input().split())) for _ in range(M)]

R = []
for i in range(M):
    radius = 10 ** 10
    e = E[i]
    for j in range(N):
        c = C[j]
        r = distance(e[0], e[1], c[0], c[1]) - c[2]
        radius = min(radius, r)
    for j in range(M):
        if i == j:
            continue
        e2 = E[j]
        r = distance(e[0], e[1], e2[0], e2[1]) / 2
        radius = min(radius, r)
    R.append(radius)

ans = 10 ** 10
for r in R:
    ans = min(ans, r)

for x, y, r in C:
    ans = min(ans, r)

print(ans)
