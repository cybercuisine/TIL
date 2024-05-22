from itertools import product

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 10 ** 12

for bits in product([0, 1], repeat=N):
    height = A[0]
    tmp = A.copy()
    cnt = 0
    count = 1
    
    for i in range(1, N):
        if bits[i] == 0:
            height = max(height, tmp[i])
            continue
        if tmp[i] <= height:
            cnt += (height - tmp[i] + 1)
            tmp[i] += (height - tmp[i] + 1)
        count += 1
        height = max(height, tmp[i])
    
    if count >= K:
        ans = min(ans, cnt)

print(ans)