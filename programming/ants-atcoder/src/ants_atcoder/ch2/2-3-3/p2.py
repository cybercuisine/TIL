H, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [float('inf')] * (3 * (10 ** 4))

for i in range(N):
    a, b = AB[i]
    dp[a] = min(dp[a], b)

for j in range(3 * (10 ** 4)):
    for i in range(N):
        a, b = AB[i]
        if j - a >= 0:
            dp[j] = min(dp[j], dp[j - a] + b)

print(min(dp[(H):]))