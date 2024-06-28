from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

MOD = 998244353

dp = [[0] * 3001 for _ in range(N)]

for j in range(A[0], B[0] + 1):
    dp[0][j] = 1

for i in range(1, N):
    cum_sum = [0] * 3001
    for j in range(3001):
        cum_sum[j] = dp[i - 1][j]
    cum_sum = list(accumulate(cum_sum))  
    for j in range(A[i], B[i] + 1):
        dp[i][j] = cum_sum[j] % MOD

result = sum(dp[N - 1][A[N - 1]:(B[N - 1] + 1)]) % MOD

print(result)
