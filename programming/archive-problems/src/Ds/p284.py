import math


T = int(input())
test = [int(input()) for _ in range(T)]

for N in test:
    p = 1
    for j in range(2, int(N ** (1/3) + 1)):
        if N % j == 0:
            p = j
            break
    if N % (p ** 2) == 0:
        print(p, N // (p ** 2))
    else:
        print(int(math.sqrt(N // j)), j)