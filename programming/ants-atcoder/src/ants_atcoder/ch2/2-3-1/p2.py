N = int(input())
P = list(map(int, input().split()))
M = 100

dp = [[False] * (N * M + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    dp[i + 1][P[i]] = True

for i in range(N):
    for j in range(N * M + 1):
        dp[i + 1][j] = dp[i][j]
        if j - P[i] >= 0:
            dp[i + 1][j] |= dp[i][j - P[i]]

ans = set()
ans.add(0)
for i in range(N + 1):
    for j in range(N * M + 1):
        if dp[i][j]:
            ans.add(j)

print(len(ans))