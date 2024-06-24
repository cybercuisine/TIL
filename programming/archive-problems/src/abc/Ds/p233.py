from collections import defaultdict
from itertools import accumulate

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

S = [0] + list(accumulate(A))

d = defaultdict(int)

ans = 0

for Sr in S:
    Sl = Sr - K
    ans += d[Sl]
    d[Sr] += 1

print(ans)
