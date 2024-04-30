N = int(input())
X = [0] * N
Y = [0] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

dp = [[1000000000.0] * N for _ in range(2**N)]
dp[0][0] = 0

for i in range(2**N):
    for j in range(N):
        if dp[i][j] < 1000000000.:
            for k in range(N):
                if (i // (2**k)) % 2 == 0:
                    DIST = ((1.0*(X[j]-X[k])* (X[j]-X[k]) + 1.0*(Y[j]-Y[k])*(Y[j]-Y[k])) ** 0.5)
                    dp[i + 2**k][k] = min(dp[i + 2**k][k], dp[i][j] + DIST)
    
print(dp[2**N - 1][0])