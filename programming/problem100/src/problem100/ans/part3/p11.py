from itertools import product

N, M = map(int, input().split())
k = []
s = []

for i in range(M):
    ki, *si = map(int, input().split())
    k.append(ki)
    s.append(si)

p = list(map(int, input().split()))

ans = 0
arr = []
for bits in product([0, 1], repeat=N):
    arr.clear()
    flg = True
    for i in range(N):
        if bits[i] == 1:
            arr.append(i + 1)
    
    for i in range(M):
        num = 0
        for j in range(k[i]):
            if s[i][j] in arr:
                num += 1
        if num % 2 != p[i]:
            flg = False
    if flg:
        ans += 1    

print(ans)