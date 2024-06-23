from collections import deque

N = int(input())
A = list(map(int, input().split()))

B = deque([])
S = 0
for i in range(N):
    S += 1
    if len(B) == 0:
        B.append([A[i], 1])
    else:
        last = B.pop()
        if last[0] != A[i]:
            B.append(last)
            B.append([A[i], 1])
        else:
            last[1] += 1
            if last[1] == last[0]:
                S -= last[0]
            else:
                B.append(last)
    print(S)