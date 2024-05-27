ans = []
while True:
    N = int(input())
    if N == 0:
        break
    w = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]

    for length in range(1, N):
        for i in range(N - length):
            j = i + length
            if length % 2 == 1:
                if dp[i+1][j-1] == length - 1:
                    if abs(w[i] - w[j]) <= 1:
                        dp[i][j] = length + 1
                    else:
                        dp[i][j] = length - 1
                for k in range(i + 1, j):
                    new = dp[i][k] + dp[k + 1][j]
                    if new > dp[i][j]:
                        dp[i][j] = new
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    ans.append(dp[0][-1])

for a in ans:
    print(a)