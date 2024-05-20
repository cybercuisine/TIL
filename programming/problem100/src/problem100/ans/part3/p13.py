from itertools import product

R, C = map(int, input().split())
senbei = [list(map(int, input().split())) for _ in range(R)]

ans = 0
arr = []
for bits in product([0, 1], repeat=R):
    arr.clear()
    for i in range(R):
        if bits[i] == 0:
            arr.append(senbei[i])
        else:
            arr.append([(senbei[i][j] + 1) % 2 for j in range(C)])
    cnt = 0
    for j in range(C):
        s = 0
        for k in range(R):
            s += arr[k][j]
        cnt += max(s, R - s)
    cnt = max(cnt, R - cnt)
    ans = max(ans, cnt)

print(ans)