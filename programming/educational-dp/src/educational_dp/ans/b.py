N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

for i in range(1, N):
    s = float('inf')
    for k in range(min(i, K) + 1):
        s = min(s, dp[i - k] + abs(h[i] - h[i - k]))
    dp[i] = s

print(dp[-1])