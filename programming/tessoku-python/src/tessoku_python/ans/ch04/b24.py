import bisect


def Get_LISValue(A):
    LEN = 0
    L = []
    for i in range(N):
        pos = bisect.bisect_left(L, A[i])
        if pos == LEN:
            L.append(A[i])
            LEN += 1
        else:
            L[pos] = A[i]
    return LEN

N = int(input())
X = [None] * N
Y = [None] * N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

WEIGHT = 0
tmp = []
for i in range(N):
    tmp.append([X[i], -Y[i]])
tmp.sort()

A = []
for i in range(N):
    A.append(-tmp[i][1])

print(Get_LISValue(A))