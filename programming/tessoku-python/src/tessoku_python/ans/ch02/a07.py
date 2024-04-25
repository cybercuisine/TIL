D = int(input())
N = int(input())
lrs = [list(map(int, input().split())) for i in range(N)]

attends = [0 for i in range(D)]

for lr in lrs:
    L = lr[0] - 1
    R = lr[1] - 1
    attends[L] += 1
    if R < D - 1:
        attends[R + 1] -= 1

for i in range(D):
    if i > 0:
        attends[i] += attends[i-1]
    print(attends[i])