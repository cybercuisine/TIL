import math
from collections import deque

def can_reach_all(S, XYP):
    N = len(XYP)
    for start in range(N):
        visited = [False] * N
        queue = deque([start])
        visited[start] = True
        count = 1
        while queue:
            i = queue.popleft()
            x1, y1, p1 = XYP[i]
            for j in range(N):
                if not visited[j]:
                    x2, y2, p2 = XYP[j]
                    if p1 * S >= abs(x1 - x2) + abs(y1 - y2):
                        visited[j] = True
                        queue.append(j)
                        count += 1
        if count == N:
            return True
    return False

def min_training(XYP):
    left, right = 0, 10 ** 20
    while left < right:
        mid = (left + right) // 2
        if can_reach_all(mid, XYP):
            right = mid
        else:
            left = mid + 1
    return left

N = int(input())
XYP = [list(map(int, input().split())) for _ in range(N)]
print(min_training(XYP))
