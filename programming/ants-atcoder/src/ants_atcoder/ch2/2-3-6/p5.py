from bisect import bisect_right

n, Q = map(int, input().split())
q = []
X = 10 ** 10
for i in range(n + Q):
    x, y = map(int, input().split())
    q += [(X - x, y, i - n)]
q.sort()
a = [0] * Q
l = [X] * (n + 1)
for x, y, z in q:
    p = bisect_right(l, y)
    if z < 0:
        l[p] = y
    else:
        a[z] = p
print(*a, sep="\n")