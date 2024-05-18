N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

X = [None] * N
Y = [None] * N
for i in range(N):
    for j in range(N):
        if P[i][j] > 0:
            X[i] = P[i][j]
            Y[j] = P[i][j]

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if X[i] > X[j]:
            ans += 1
            X[i], X[j] = X[j], X[i]
        if Y[i] > Y[j]:
            ans += 1
            Y[i], Y[j] = Y[j], Y[i]

print(ans)