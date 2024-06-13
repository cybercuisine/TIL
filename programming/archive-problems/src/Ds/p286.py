N, X = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [False] * (X + 1)
dp[0] = True

for a, b in AB:
    for j in range(X, -1, -1):
        if dp[j]:
            for k in range(1, b + 1):
                if j + a * k <= X:
                    dp[j + a * k] = True
                else:
                    break

flg = dp[X]
print("Yes" if flg else "No")
