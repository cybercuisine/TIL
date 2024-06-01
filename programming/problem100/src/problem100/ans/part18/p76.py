N = int(input())
A = list(map(int, input().split()))

S = []
for i in range(N):
    if i == 0:
        S.append(A[i])
    else:
        S.append(A[i] + S[i - 1])

ans = []
for k in range(N):
    cnt = 0
    for i in range(k, N):
        s = S[i - k - 1] if i - k - 1 >= 0 else 0
        cnt = max(cnt, S[i] - s)
    ans.append(cnt)

print(*ans, sep="\n")