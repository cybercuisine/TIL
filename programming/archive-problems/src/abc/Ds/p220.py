N = int(input())
A = list(map(int, input().split()))

MOD = 998244353

dp = [[0] * 10 for _ in range(N)]
dp[0][A[0]] = 1

for i in range(1, N):
    for j in range(10):
        x = j
        y = A[i]
        f = (x + y) % 10
        g = (x * y) % 10
        dp[i][f] += dp[i - 1][x]
        dp[i][g] += dp[i - 1][x]
    
    for j in range(10):
        dp[i][j] %= MOD

print(*dp[-1], sep='\n')