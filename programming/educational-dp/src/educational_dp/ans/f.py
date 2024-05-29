s = input()
t = input()
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

for i, vi in enumerate(s):
    for j, vj in enumerate(t):
        if vi == vj:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

ans = []
i = len(s) - 1
j = len(t) - 1
while i >= 0 and j >= 0:
    if s[i] == t[j]:
        ans.append(s[i])
        i -= 1
        j -= 1
    elif dp[i+1][j+1] == dp[i][j+1]:
        i -= 1
    elif dp[i+1][j+1] == dp[i+1][j]:
        j -= 1

ans.reverse()
print(*ans, sep='')