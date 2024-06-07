N = int(input())
k = -1
for i in range(1, N + 5):
    if i * (i - 1) // 2 == N:
        k = i
        break
if k == -1:
    print('No')
    exit()

cnt = 0
s = [set() for _ in range(k)]
for i in range(k):
    for j in range(i + 1, k):
        s[i].add(cnt + 1)
        s[j].add(cnt + 1)
        cnt += 1

print('Yes')
print(len(s))
for v in s:
    print(len(v), *v)