N = int(input())
A = list(map(int, input().split()))

prev = ''
cnt = 0
left = []

for a in A:
    if a == prev:
        left.append(cnt)
        cnt = 1
    else:
        cnt += 1
    prev = a
left.append(cnt)
left += [0, 0]

ans = 0
for i in range(len(left) - 2):
    ans = max(ans, sum(left[i:i+3]))
print(ans)