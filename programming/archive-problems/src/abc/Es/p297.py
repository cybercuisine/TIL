from sortedcontainers import SortedSet

def MI():
    return map(int, input().split())


N, K = MI()
A = list(MI())

S = SortedSet([0])
for i in range(K):
    s = S.pop(0)
    for i in range(N):
        S.add(s + A[i])

print(S.pop(0))

"""
from collections import deque


def MI():
    return map(int, input().split())


N, K = MI()
A = list(MI())

def count_ways_up_to_x(x):
    dp = set()
    queue = deque([0])
    while queue:
        current = queue.popleft()
        if current > x:
            continue
        if current not in dp:
            if current != 0:
                dp.add(current)
            if len(dp) >= K:
                return K
            for a in A:
                if current + a <= x:
                    queue.append(current + a)
    return len(dp)

A.sort()

left = 1
right = 2 * 10**14

while right - 1 > left:
    mid = (left + right) // 2
    if count_ways_up_to_x(mid) >= K:
        right = mid
    else:
        left = mid


print(right)
"""
