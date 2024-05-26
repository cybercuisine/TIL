Q = int(input())
X = []
Y = []
for i in range(2*Q):
    if i % 2 == 0:
        X.append(input())
    else:
        Y.append(input())

answers = []
for i in range(Q):
    x, y = X[i], Y[i]
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    
    for i, vi in enumerate(x):
        for j, vj in enumerate(y):
            if vi == vj:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    answers.append(dp[len(x)][len(y)])

for ans in answers:
    print(ans)