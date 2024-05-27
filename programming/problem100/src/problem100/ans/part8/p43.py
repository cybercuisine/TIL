N = int(input())
S = []
col = {'R':0, 'B':1, 'W':2, '#':-1}
for i in range(5):
    s = input()
    ls = list(s)
    ls = [-1] + [col[e] for e in ls]
    S.append(ls)
dp = [[0]*3 for _ in range(N+1)]

dp = [[0, 0, 0] for _ in range(N + 1)]

for n in range(N):
    for i in range(3):
        cnt = 0
        for j in range(5):
            cnt += (S[j][n + 1] != i)
        K = [0, 1, 2]
        K.remove(i)
        dp[n + 1][i] = min(dp[n][K[0]] + cnt, dp[n][K[1]] + cnt)

print(min(dp[-1]))