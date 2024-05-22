from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

arrays = list(permutations([i for i in range(1, N + 1)]))
arrays.sort()

a = 0
b = 0
for i in range(len(arrays)):

    if P == list(arrays[i]):
        a = i
    if Q == list(arrays[i]):
        b = i

print(abs(a - b))