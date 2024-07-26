def MI():
    return map(int, input().split())

W, N = MI()
LRV = [list(MI()) for _ in range(N)]

dp = [-1] * (W + 1)  
dp[0] = 0  

for left, right, v in LRV:
    for j in reversed(range(W)):
        if dp[j] != -1 and j + left <= W:
            dp[j + left] = max(dp[j] + v, dp[j + left])
            if j + right < W:
                dp[j + right] = max(dp[j] + v, dp[j + right])
            elif W <= j + right:
                dp[W] = max(dp[j] + v, dp[W])

print(dp[W])