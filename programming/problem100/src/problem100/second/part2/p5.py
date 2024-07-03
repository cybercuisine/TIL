M = int(input())
stars = [list(map(int, input().split())) for _ in range(M)]
N = int(input())
photos = [list(map(int, input().split())) for _ in range(N)]

S = set()
for x, y in photos:
    S.add((x, y))

for i in range(N):
    px, py = photos[i]
    for j in range(M):
        sx, sy = stars[j]
        dx, dy = sx - px, sy - py
        flg = True
        for k in range(M):
            tx, ty = stars[k]
            if (tx - dx, ty - dy) not in S:
                flg = False
        if flg:
            print(-dx, -dy)
            exit()