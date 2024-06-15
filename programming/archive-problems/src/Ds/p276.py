import math
from typing import List
from functools import reduce
from collections import Counter

def all_gcd(arr: List[int]) -> int:
    return reduce(math.gcd, arr)

def dividable(x: int) -> int:
    if x == 1:
        return 0
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    while x % 3 == 0:
        x //= 3
        cnt += 1
    if x != 1:
        return -1
    return cnt

N = int(input())
A = list(map(int, input().split()))
A.sort()

gcds = all_gcd(A)

for i in range(N):
    A[i] //= gcds

cnts = Counter(A)
keys = list(cnts.keys())

ans = 0
for key in keys:
    steps = dividable(key)
    if steps == -1:
        print(-1)
        exit()
    ans += cnts[key] * steps

print(ans)

