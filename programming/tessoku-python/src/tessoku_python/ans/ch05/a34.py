N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

grundy = [None] * (100001)
for i in range(100001):
    transit = [False, False, False]
    if i >= X:
        transit[grundy[i-X]] = True
    if i >= Y:
        transit[grundy[i-Y]] = True
    
    if transit[0] == False:
        grundy[i] = 0
    elif transit[1] == False:
        grundy[i] = 1
    else:
        grundy[i] = 2

xor_sum = 0
for i in range(N):
    xor_sum ^= grundy[A[i]]

if xor_sum >= 1:
    print("First")
else:
    print("Second")