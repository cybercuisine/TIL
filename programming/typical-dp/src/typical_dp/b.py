A, B = map(int, input().split())
N = A + B
a = list(map(int, input().split()))
b = list(map(int, input().split()))


dp = [[0] * (B + 1) for _ in range(A + 1)]

for i in range(A + 1):
    for j in range(B + 1):
        if i == 0 and j == 0:
            continue
        if (N - i - j) % 2 == 0:
            if i == 0:
                dp[0][j] = dp[0][j - 1] + b[B - j]
            elif j == 0:
                dp[i][0] = dp[i - 1][0] + a[A - i]
            else:
                dp[i][j] = max(dp[i - 1][j] + a[A - i], dp[i][j - 1] + b[B - j])
        else:
            if i == 0:
                dp[0][j] = dp[0][j - 1]
            elif j == 0:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])

print(dp[A][B])