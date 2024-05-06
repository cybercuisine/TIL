N = int(input())
A = list(map(int, input().split()))

dp = [[None] * i for i in range(1, N)]
dp.append(A)

for i in reversed(range(N - 1)):
    for j in range(i + 1):
        if i % 2 == 0:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])