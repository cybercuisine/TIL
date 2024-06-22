"""AtCoder Beginner Contest 271 D"""
n, s = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

dp = [[False for i2 in range(s + 1)] for i1 in range(n + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(s + 1):
        if j - a[i] >= 0 and dp[i][j - a[i]]:
            dp[i + 1][j] = True
        if j - b[i] >= 0 and dp[i][j - b[i]]:
            dp[i + 1][j] = True

if dp[n][s]:
    print("Yes")

    t = ""
    for i in range(n-1, -1, -1):
        if s - a[i] >= 0 and dp[i][s - a[i]]:
            t = "H" + t
            s -= a[i]
        else:
            t = "T" + t
            s -= b[i]
    print(t)
else:
    print("No")