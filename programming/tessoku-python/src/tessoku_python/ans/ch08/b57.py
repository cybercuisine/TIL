N, K = map(int, input().split())

dp = [[0] * 300009 for _ in range(30)]

for i in range(N + 1):
    dp[0][i] = i - sum(map(int, str(i)))

for d in range(29):
    for i in range(N + 9):
        dp[d + 1][i] = dp[d][dp[d][i]]

for i in range(1, N + 1):
    num = i
    for d in range(30):
        if K & (1 << d):
            num = dp[d][num]
    print(num)