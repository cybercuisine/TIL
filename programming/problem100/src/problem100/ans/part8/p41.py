D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
ABC = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[-(10 ** 10)] * N for _ in range(D + 1)]

for i in range(D):
    t = T[i]
    for j in range(N):
        a = ABC[j][0]
        b = ABC[j][1]
        c = ABC[j][2]
        if a <= t <= b:
            if i == 0:
                dp[i + 1][j] = 0
                continue
            for m in range(N):
                cm = ABC[m][2]
                dp[i + 1][j] = max(dp[i][m] + abs(c - cm), dp[i + 1][j])

print(max(dp[-1]))