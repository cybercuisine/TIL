N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for i in range(Q)]

dp = [[0] * N for i in range(30)]
for i in range(N):
    dp[0][i] = A[i] - 1

for d in range(1, 30):
    for i in range(N):
        dp[d][i] = dp[d-1][dp[d-1][i]]

for x,y in queries:
    current_place = x - 1
    for d in range(29, -1, -1):
        if ((y >> d) & 1) == 1:
            current_place = dp[d][current_place]
    print(current_place + 1)