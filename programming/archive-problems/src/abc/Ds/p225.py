N, Q = map(int, input().split())

train = [[-1, -1] for _ in range(N + 1)]
queries = [list(map(int, input().split())) for _ in range(Q)]

for i in range(Q):
    query = queries[i]
    if query[0] == 1:
        x,y = query[1],query[2]
        train[x][1], train[y][0] = y,x
    elif query[0] == 2:
        x,y = query[1],query[2]
        train[x][1], train[y][0] = -1,-1
    else:
        x = query[1]
        front = []
        back = []
        f = train[x][0]
        b = train[x][1]
        while f != -1:
            front.append(f)
            f = train[f][0]
        while b != -1:
            back.append(b)
            b = train[b][1]
        ans = front[::-1] + [x] + back
        print(len(ans), *ans)