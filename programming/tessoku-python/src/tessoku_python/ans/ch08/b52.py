from collections import deque

N, X = map(int, input().split())
X -= 1
A = list(input())

S = deque([X])
S.append(X)
A[X] = '@'

while len(S) > 0:
    s = S.popleft()
    if s - 1 >= 0 and A[s-1] == ".":
        A[s-1] = '@'
        S.append(s - 1)
    if s + 1 < N and A[s + 1] == ".":
        A[s + 1] = '@'
        S.append(s + 1)

print("".join(A))