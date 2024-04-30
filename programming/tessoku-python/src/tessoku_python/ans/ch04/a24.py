import bisect

N = int(input())
A = list(map(int, input().split()))

LEN = 0
L = []
dp = [None] * N

for i in range(N):
    pos = bisect.bisect_left(L, A[i])
    dp[i] = pos
    
    if dp[i] >= LEN:
        L.append(A[i])
        LEN += 1
    else:
        L[dp[i]] = A[i]

print(LEN)