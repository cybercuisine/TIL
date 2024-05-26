N, W = map(int, input().split())
values = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (W + 1)

for i in range(N):
    value, weight = values[i]
    for w in range(weight, W + 1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(max(dp))
