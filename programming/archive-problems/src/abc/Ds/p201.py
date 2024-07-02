H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]


dp = [[-float('inf')] * W for _ in range(H)]
dp[-1][-1] = 0

for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        if i + 1 < H:
            dp[i][j] = max(dp[i][j], -dp[i + 1][j] + (1 if A[i + 1][j] == '+' else -1))
        if j + 1 < W:
            dp[i][j] = max(dp[i][j], -dp[i][j + 1] + (1 if A[i][j + 1] == '+' else -1))



if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] < 0:
    print("Aoki")
else:
    print("Draw")