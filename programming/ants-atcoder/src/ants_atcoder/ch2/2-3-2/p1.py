N = int(input())
X = []
Y = []
for i in range(N):
    x = input()
    y = input()
    X.append(x)
    Y.append(y)

answers = []
for x, y in zip(X, Y):
    nx = len(x)
    ny = len(y)
    dp = [[0] * (nx + 1) for _ in range(ny + 1)]
    for i in range(1, ny + 1):
        for j in range(1, nx + 1):
            s = 1 if x[j - 1] == y[i - 1] else 0
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+ s)
    print(dp[-1][-1])