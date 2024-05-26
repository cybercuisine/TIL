N = int(input())
X = list(map(int, input().split()))

left = X[:(len(X) - 1)]
right = X[-1]

dp = [[0] * 21 for _ in range(N + 1)]

dp[1][left[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        pls = j + left[i]
        mns = j - left[i]

        if pls <= 20:
            dp[i + 1][pls] += dp[i][j]
        if mns >= 0:
            dp[i + 1][mns] += dp[i][j]

print(dp[N - 1][right])