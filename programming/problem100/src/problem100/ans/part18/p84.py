N, M = map(int, input().split())
ABX = [list(map(int, input().split())) for _ in range(M)]

C = [[0] * (N + 10) for _ in range(N + 10)]

for A, B, X in ABX:
    C[A][B] += 1
    C[A][B + 1] -= 1
    C[A + X + 1][B] -= 1
    C[A + X + 1][B + X + 2] += 1
    C[A + X + 2][B + 1] += 1
    C[A + X + 2][B + X + 2] -= 1

for i in range(N + 2):
    for j in range(N + 1):
        C[i][j + 1] += C[i][j]

for i in range(N + 1):
    for j in range(N + 2):
        C[i + 1][j] += C[i][j]

for i in range(N + 1):
    for j in range(N + 1):
        C[i + 1][j + 1] += C[i][j]

ans = 0
for i in range(1, N + 1):
    for j in range(1, i + 1):
        if C[i][j] >= 1:
            ans += 1

print(ans)