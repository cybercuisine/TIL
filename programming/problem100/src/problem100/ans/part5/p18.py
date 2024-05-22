import bisect

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

C = 0

for t in T:
    idx = bisect.bisect_right(S, t)
    if S[idx-1] == t:
        C += 1

print(C)