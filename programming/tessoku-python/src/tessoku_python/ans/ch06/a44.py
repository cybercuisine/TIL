N, Q = map(int, input().split())
A = [i for i in range(1, N + 1)]

ans = []
rev = False
query = []

for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if rev:
            A[N - query[1]] = query[2]
        else:
            A[query[1] - 1] =  query[2]
    elif query[0] == 2:
        rev = not bool(rev)
    else:
        if rev:
            ans.append(A[N - query[1]])
        else:
            ans.append(A[query[1] - 1])

for a in ans:
    print(a)