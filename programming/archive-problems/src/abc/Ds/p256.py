from collections import deque
from itertools import accumulate

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

LR.sort()

S = [0] * (2 * (10 ** 5) + 1)

for l, r in LR:
    S[l] += 1
    S[r] -= 1

S = list(accumulate(S))

prev = 0
XY = []
for i in range(1, 2 * (10 ** 5) + 1):
    if S[i] > 0 and S[i - 1] == 0:
        prev = i
    if S[i] == 0 and S[i - 1] > 0:
        XY.append([prev, i])

for xy in XY:
    print(*xy)