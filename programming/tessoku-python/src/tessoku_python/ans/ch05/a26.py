import math

def prime_check(N):
    root = int(N ** 0.5)
    for i in range(2, root + 1):
        if N % i == 0:
            return False
    return True

Q = int(input())
X = [int(input()) for _ in range(Q)]

for x in X:
    if prime_check(x):
        print("Yes")
    else:
        print("No")