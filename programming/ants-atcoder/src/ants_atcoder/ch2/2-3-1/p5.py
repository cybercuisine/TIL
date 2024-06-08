D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
ABC = [list(map(int, input().split())) for _ in range(N)]

dp = [[-10 ** 10] * N for i in range(D)]

prev = 0
for i in range(D):
    t = T[i]
    for j in range(N):
        a, b, c = ABC[j]
        if a <= t <= b:
            if i == 0:
                dp[i][j] = 0
                continue
            for m in range(N):
                cm = ABC[m][2]
                dp[i][j] = max(dp[i - 1][m] + abs(c - cm), dp[i][j])

print(max(dp[-1]))