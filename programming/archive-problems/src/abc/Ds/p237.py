from collections import deque

N = int(input())
S = input()


A = deque([N])

for i in range(N - 1, -1, -1):
    si = S[i]
    if si == 'L':
        A.append(i)
    else:
        A.appendleft(i)

print(*A)