N = int(input())
A = [int(input()) for _ in range(N)]
if N == 1:
    print(A[0])
    exit()
dp = [[0] * (2 * N) for _ in range(2 * N)]

if N % 2 == 1:
    for i in range(2 * N):
        dp[i][i] = A[i % N]

for i in range(1, N):
    for L in range(2*N - 2 - i):
        R = L + i
        if (N - (i + 1)) % 2 == 1:
            dp[L][R] = dp[L][R - 1] if A[R % N] > A[L % N] else dp[L + 1][R]
        else:
            dp[L][R] = max(dp[L][R - 1] + A[R % N], dp[L + 1][R] + A[L % N])

ans = 0
for i in range(N):
    ans = max(ans, dp[i][i+N-1])
print(ans)