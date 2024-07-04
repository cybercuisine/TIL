from itertools import product

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = float('inf')

for bits in product([0, 1], repeat=N):
    M = A[0]
    cnt = 0
    hcnt = 1
    for i in range(1, N):
        if bits[i] == 0:
            if A[i] > M:
                hcnt += 1
                M = A[i]
            continue
        cnt += max(M + 1 - A[i], 0)
        M = max(A[i], M + 1)
        hcnt += 1

    
    if hcnt >= K:
        ans = min(cnt, ans)

print(ans)