from itertools import accumulate

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

S = [[0] * 1002 for _ in range(1002)]

for lx, ly, rx, ry in L:
    S[ly][lx] += 1
    S[ry][rx] += 1
    S[ly][rx] -= 1
    S[ry][lx] -= 1

for i in range(1002):
    S[i] = list(accumulate(S[i]))

for j in range(1002):
    for i in range(1, 1002):
        S[i][j] += S[i - 1][j]

ans = [0] * (N + 1)
for i in range(1002):
    for j in range(1002):
        ans[S[i][j]] += 1

print(*ans[1:], sep='\n')
