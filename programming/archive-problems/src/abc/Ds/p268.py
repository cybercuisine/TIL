import sys
from itertools import permutations

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

if N == 1:
    if 3 <= len(S[0]) <= 16 and S[0] not in T:
        print(S[0])
    else:
        print(-1)
    exit()

memo = [[[] for _ in range(17)] for _ in range(17)]

def DFS(rem, depth):
    if memo[rem][depth]:
        return memo[rem][depth]
    if rem <= 0 or depth == 0:
        return []
    if depth == N - 1:
        return [[i] for i in range(1, rem + 1)]
    ret = []
    for i in range(1, rem + 1):
        for j in DFS(rem - i, depth + 1):
            ret.append([i] + j)
    memo[rem][depth] = ret
    return ret

su = 16 - sum(len(i) for i in S)
L = DFS(su, 1)

for p in permutations(S):
    for l in L:
        now = ""
        for i in range(N - 1):
            now += p[i]
            now += l[i] * "_"
        now += p[-1]
        if not 3 <= len(now) <= 16:
            continue
        if now not in T:
            print(now)
            exit()

print(-1)
