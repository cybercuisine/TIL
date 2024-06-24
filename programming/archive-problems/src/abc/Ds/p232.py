H, W = map(int, input().split())
C = [input() for _ in range(H)]

dp = [[-float('inf')] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i == j == 0:
            continue
        if C[i][j] == ".":
            d1 = dp[i - 1][j] if i - 1 >= 0 else -float('inf')
            d2 = dp[i][j - 1] if j - 1 >= 0 else -float('inf')
            dp[i][j] = max(d1, d2) + 1

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, dp[i][j])

print(ans)