import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [A[i] for i in range((N-1)//2 + 1)]
C = [A[i] for i in range((N-1)//2 + 1, N)]

D = []
E = []

for i in range(2**len(B)):
    t = 0
    for j in range(len(B)):
        if ((i >> j) & 1):
            t += B[j]
    D.append(t)

for i in range(2**len(C)):
    t = 0
    for j in range(len(C)):
        if ((i >> j) & 1):
            t += C[j]
    E.append(t)

ans = "No"
D.sort()
E.sort()

if K in D or K in E:
    ans = "Yes"

for d in D:
    f = K - d
    mid = bisect.bisect(E, f)
    if E[mid-1] == f:
        ans = "Yes"
        break

print(ans)