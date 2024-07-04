from itertools import permutations


N = int(input())
L = [i + 1 for i in range(N)]
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

a = 0
b = 0

i = 1
for seq in list(permutations(L)):
    if list(seq) == P:
        a = i
    if list(seq) == Q:
        b = i
    i += 1

print(abs(a - b))