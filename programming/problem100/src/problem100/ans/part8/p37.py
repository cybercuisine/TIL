INF = 10 ** 10

N, M = map(int, input().split())
C = list(map(int, input().split()))

dp = [INF] * 50009
dp[0] = 0
for c in C:
    dp[c] = 1

for i in range(N + 1):
    for j in range(M):
        c = C[j]
        if i >= c:
            dp[i] = min(dp[i-c] + 1, dp[i])
        

print(dp[N])