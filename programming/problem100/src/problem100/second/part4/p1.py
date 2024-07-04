from itertools import permutations
import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

P = list(permutations(XY))
total = 0
for seq in P:
    x, y = seq[0]
    for i in range(1, N):
        x1, y1 = seq[i]
        total += math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        x, y = x1, y1

ans = total / len(P)
print(ans)