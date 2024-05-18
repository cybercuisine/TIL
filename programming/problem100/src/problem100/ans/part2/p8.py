N = int(input())
customer = [list(map(int, input().split())) for _ in range(N)]


ans = 10 ** 15
for i in range(N):
    for j in range(N):
        entrance = customer[i][0]
        exits = customer[j][1]
        if entrance > exits:
            continue
        cnt = 0
        for k in range(N):
            a = customer[k][0]
            b = customer[k][1]
            cnt += (exits - entrance) + max(0, 2 * (entrance - a)) + max(0, 2 * (b - exits))
        ans = min(ans, cnt)

print(ans)