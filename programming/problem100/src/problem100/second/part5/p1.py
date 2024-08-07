import bisect


N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

S.sort()
ans = 0
for t in T:
    idx = bisect.bisect_left(S, t)
    if idx < N and S[idx] == t:
        ans += 1

print(ans)