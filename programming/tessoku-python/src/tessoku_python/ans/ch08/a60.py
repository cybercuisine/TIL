from collections import deque

N = int(input())
A = list(map(int, input().split()))


ans = [None] * N
level2 = deque()

for i in range(N):
    if i >= 1:
        level2.append((i, A[i - 1]))
        while len(level2) >= 1:
            kabuka = level2[-1][1]
            if kabuka <= A[i]:
                level2.pop()
            else:
                break
    if len(level2) >= 1:
        ans[i] = level2[-1][0]
    else:
        ans[i] = -1

print(*ans)