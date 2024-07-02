N = int(input())
T = list(map(int, input().split()))

S = sum(T)
S = S // 2 + S % 2
dp = [[False] * 10 ** 5 for _ in range(N + 1)]
dp[0][0] = True

ans = float('inf')

for i in range(1, N + 1):
    t = T[i - 1]
    for j in range(10 ** 5):
        dp[i][j] = dp[i - 1][j]
        if j - t >= 0:
            dp[i][j] |= dp[i - 1][j - t]
        if j >= S and dp[i][j]:
            ans = min(ans, j)

print(ans)