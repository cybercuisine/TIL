N = int(input())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

Q = int(input())
query = []
ans = []

for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A[query[1] - 1], A[query[2] - 1] = A[query[2] - 1], A[query[1] - 1]
    else:
        ans.append(A[query[1] - 1][query[2] - 1])

for a in ans:
    print(a)