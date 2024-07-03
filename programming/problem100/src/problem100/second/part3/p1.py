N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))


dp = [[False] * 2001 for _ in range(N)]
dp[0][0] = True
dp[0][A[0]] = True

for i in range(1, N):
    for j in range(2001):
        dp[i][j] = dp[i - 1][j]
        if j - A[i] >= 0:
            dp[i][j] |= dp[i - 1][j - A[i]]


for m in M:
    if dp[-1][m]:
        print("yes")
    else:
        print("no")