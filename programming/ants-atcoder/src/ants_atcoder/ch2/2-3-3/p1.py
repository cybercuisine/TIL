N, W = map(int, input().split())
VW = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (W + 1)
for j in range(W + 1):
    for i in range(N):
        v, w = VW[i]
        if w <= j:
            dp[j] = max(dp[j], dp[j - w] + v)
print(dp[-1])