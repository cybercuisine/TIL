from itertools import product

N, M = map(int, input().split())
K, S = [], []
for i in range(M):
    k, *s = map(int, input().split())
    K.append(k)
    S.append(s)
P = list(map(int, input().split()))


ans = 0
for bits in product([0, 1], repeat=N):
    flg = True
    for i in range(M):
        cnt = 0
        for j in range(K[i]):
            if bits[S[i][j] - 1] == 1:
                cnt += 1
        if cnt % 2 != P[i]:
            flg = False
            break

    if flg:
        ans += 1

print(ans)