N = int(input())
abc = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = abc[0]

for i in range(1, N):
    a, b, c = abc[i]
    for j in range(3):
        if j == 0:
            dp[i][j] = max(dp[i-1][1] + a, dp[i-1][2] + a)
        elif j == 1:
            dp[i][j] = max(dp[i-1][0] + b, dp[i-1][2] + b)
        else:
            dp[i][j] = max(dp[i-1][0] + c, dp[i-1][1] + c)

print(max(dp[-1]))
