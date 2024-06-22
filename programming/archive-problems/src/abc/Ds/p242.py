def rec(t, k):
    if t == 0:
        return pat.index(S[k])
    if k == 0:
        return pat.index(S[0]) + t
    if k % 2 == 0:
        return rec(t - 1, k // 2) + 1
    else:
        return rec(t - 1, k // 2) + 2

def solve():
    t, k = map(int, input().split())
    k -= 1
    return pat[rec(t, k) % 3]

S = input()
Q = int(input())
pat = "ABC"
for _ in range(Q):
    print(solve())