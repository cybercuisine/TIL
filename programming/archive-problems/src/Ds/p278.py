from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
g = 0
base = 0
diff = defaultdict(int)


q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
for t in query:
    if t[0] == 1:
        g += 1
        base = t[1]
    elif t[0] == 2:
        diff[(g, t[1])] += t[2]
    else:
        if g > 0:
            print(base + diff[(g, t[1])])
        else:
            print(a[t[1] - 1] + diff[(g, t[1])])