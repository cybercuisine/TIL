N = int(input())
SLP = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
W = [int(input()) for _ in range(M)]
max_w = max(W)

dp = [[0] * (max_w + 1) for _ in range(N)]

for i in range(N):
    s, l, p = SLP[i]
    for j in range(max_w + 1):
        if i >= 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        for k in range(s, l + 1):
            if j - k >= 0:
                dp[i][j] = max(dp[i][j], dp[i][j - k] + p)

ans = []
for w in W:
    if dp[N - 1][w] > 0:
        ans.append(dp[N - 1][w])
    else:
        print(-1)
        exit()

print(*ans, sep='\n')