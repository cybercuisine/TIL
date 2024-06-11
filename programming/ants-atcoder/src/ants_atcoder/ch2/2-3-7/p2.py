N,M = map(int,input().split())
KA = list(map(int,input().split()))
KB = list(map(int,input().split()))
MOD = 10**9+7

P = [[0]*(1001) for _ in range(101)]
P[0][0] = 1
for i in range(1,101):
    for j in range(1001):
        if j-i >= 0:
            P[i][j] = P[i][j-i] + P[i-1][j]
            P[i][j] %= MOD
        else:
            P[i][j] = P[i-1][j]

from collections import Counter
def solve(kill, sum_death):
    C = Counter(kill)
    dp = [0]*(sum_death+1)
    dp[sum_death] = 1
    for v in C.values():
        ndp = [0]*(sum_death+1)
        for i in range(sum_death+1):
            for j in range(sum_death+1):
                if i-j < 0: break
                ndp[i-j] += dp[i]*P[v][j]
                ndp[i-j] %= MOD
        dp = ndp
    return dp[0]

print(solve(KA,sum(KB)) * solve(KB,sum(KA)) % MOD)