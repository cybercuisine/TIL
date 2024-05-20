from typing import List
from itertools import product

def check(A: List[int], m: int) -> bool:
    # n = len(A)
    dp = [False] * (m + 1)
    dp[0] = True

    for num in A:
        for j in range(m, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
    return dp[m]


n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

for mi in m:
    if check(A, mi):
        print("yes")
    else:
        print("no")