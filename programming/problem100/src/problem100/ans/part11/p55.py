from bisect import bisect_right, bisect_left

def LIS(L):
    INF = float('inf')
    n = len(L)
    dp = [INF] * n

    for i in range(n):
        pos = bisect_right(dp, L[i])
        dp[pos] = L[i]
    return bisect_left(dp, INF)

N = int(input())
A = [int(input()) for _ in range(N)]
A.reverse()

print(LIS(A))