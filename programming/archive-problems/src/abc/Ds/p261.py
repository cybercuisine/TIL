N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for _ in range(M)]

CY_dict = {}
for c, y in CY:
    CY_dict[c] = y

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    prev_max = 0
    for j in range(N + 1):
        if j > i:
            break
        s = 0 if j not in CY_dict else CY_dict[j]
        if j == 0:
            dp[i][j] = prev_max
        else:
            dp[i][j] = dp[i - 1][j - 1] + X[i - 1] + s
        dp[i][0] = max(dp[i][0], dp[i - 1][j])
        prev_max = max(prev_max, dp[i][j])

print(max(dp[-1]))