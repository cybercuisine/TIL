N = int(input())
S = list(input())

# i 回目に j を出して勝つ
# j = 0: G,  j = 1: P,  j = 2: S
dp = [[0, 0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(3):
        others = []
        for k in range(3):
            if j != k:
                others.append(dp[i - 1][k])
        dp[i][j] = max(others)
        if S[i - 1] == "R":
            if j == 1:
                dp[i][j] += 1
            elif j == 2:
                dp[i][j] = 0
        elif S[i - 1] == "P":
            if j == 2:
                dp[i][j] += 1
            elif j == 0:
                dp[i][j] = 0
        elif S[i - 1] == "S":
            if j == 0:
                dp[i][j] += 1
            elif j == 1:
                dp[i][j] = 0

print(max(dp[N]))
