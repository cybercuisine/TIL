T = int(input())
N = int(input())
lrs = [list(map(int, input().split())) for i in range(N)]

B = [0 for i in range(T)]

for lr in lrs:
    L = lr[0]
    R = lr[1]
    B[L] += 1
    if R < T:
        B[R] -= 1

for i in range(T):
    if i > 0:
        B[i] += B[i - 1]
    print(B[i])
