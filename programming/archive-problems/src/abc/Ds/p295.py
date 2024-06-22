from collections import defaultdict

S = list(input())
d = defaultdict(int)
bit = 0
d[0] = 1
for s in S:
    s = int(s)
    bit ^= (1 << s)
    d[bit] += 1

ans = 0
for key in d:
    n = d[key]
    ans += n * (n - 1) // 2

print(ans)