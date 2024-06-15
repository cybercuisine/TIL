from collections import defaultdict,Counter

N, M = [int(nm) for nm in input().split()]
A = [int(a) for a in input().split()]
X = Counter(A)
AA = set(A)
B = defaultdict(int)
tmp = 0

for a in sorted(AA):
    tmp += a * X[a]
    if (a + 1) % M not in AA:
        B[a % M] = tmp
        tmp = 0

if tmp > 0:
    AA.add(10 ** 10)
    for i, a in enumerate(sorted(AA)):
        if i != a:
            B[i - 1] += tmp
            break

accA = sum(A)
ans = 10 ** 20
for b in B:
    ans = min(ans, accA - B[b])

print(ans)
