# TLE in python, MLE in PyPy when use dp[N][K][W], so we need memory savings.
W = int(input())
N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

# compare with dp[N][K][W], dp_prev means dp[n - 1], dp_curr means dp[n]
dp_prev = [[0] * (W + 1) for _ in range(K + 1)]
dp_curr = [[0] * (W + 1) for _ in range(K + 1)]

for n in range(1, N + 1):  
    a, b = AB[n - 1]
    for k in range(1, K + 1):
        for w in range(W + 1):
            dp_curr[k][w] = dp_prev[k][w]
            if w - a >= 0:
                dp_curr[k][w] = max(dp_curr[k][w], dp_prev[k - 1][w - a] + b)
    # swap dp_prev, dp_curr
    dp_prev, dp_curr = dp_curr, dp_prev

print(dp_prev[K][W])
