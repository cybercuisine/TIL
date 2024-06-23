from sortedcontainers import SortedList

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sa = SortedList(A)

ans = 0
for b in B:
    idx = sa.bisect_left(b)
    if idx >= len(sa):
        print(-1)
        exit()
    
    ans += sa[idx]
    sa.remove(sa[idx])

print(ans)