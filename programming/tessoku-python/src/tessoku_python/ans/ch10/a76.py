import bisect

N, W, L, R = map(int, input().split())
X = [0] + list(map(int, input().split())) + [W]
N += 2
wari = 1000000007

dp = [0] * N
dpsum = [0] * N
dp[0] = 1
dpsum[0] = 1

for i in range(1, N):
    posR = bisect.bisect_left(X, X[i] - L + 1) - 1
    posL = bisect.bisect_left(X, X[i] - R) - 1
    dp[i] = (dpsum[posR] if posR >= 0 else 0) - (dpsum[posL] if posL >= 0 else 0)
    dp[i] %= wari
    dpsum[i] = (dpsum[i-1] + dp[i]) % wari
    
print(dp[-1])