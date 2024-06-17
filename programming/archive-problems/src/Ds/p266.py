from collections import defaultdict

N = int(input())
TXA = [list(map(int, input().split())) for _ in range(N)]

M = defaultdict(dict)
for t, x, a in TXA:
    if a in M[t]:
        M[t][x] = max(a, M[t][x])
    else:
        M[t][x] = a

MAX_T = 10 ** 5 + 1
dp = [[0] * (5) for _ in range(MAX_T)]

for i in range(1, MAX_T):
    for j in range(5):
        if i < j:
            continue
        dp[i][j] = dp[i - 1][j]
        if 0 <= j - 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
        if j + 1 <= 4:
            dp[i][j] = max(dp[i][j], dp[i - 1][j + 1])
        if j in M[i]:
            dp[i][j] += M[i][j]
    
print(max(dp[-1]))

