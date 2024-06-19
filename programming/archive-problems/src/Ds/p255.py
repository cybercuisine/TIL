import bisect
from itertools import accumulate

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
X = [int(input()) for _ in range(Q)]

S = list(accumulate(A))

for x in X:
    idx = bisect.bisect_left(A, x)
    
    smaller = 0
    if idx > 0:
        smaller += idx * x - S[idx - 1]
    
    larger = 0
    if idx < N:
        larger += S[-1] -(S[idx - 1] if idx > 0 else 0) - (N - idx) * x
    
    print(smaller + larger)