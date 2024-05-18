M = int(input())
seiza = [list(map(int, input().split())) for _ in range(M)]

N = int(input())
stars = [list(map(int, input().split())) for _ in range(N)]

target_diff = [(0,0)]
for i in range(1, M):
    target_diff.append((seiza[i][0] - seiza[0][0], seiza[i][1] - seiza[0][1]))

star_dict = {}
for x, y in stars:
    if x not in star_dict:
        star_dict[x] = []
    star_dict[x].append(y)

selected = []
for i in range(N):
    selected = []
    flg = True
    x = stars[i][0]
    y = stars[i][1]
    for diff in target_diff:
        dx = diff[0]
        dy = diff[1]
        if x + dx not in star_dict or y + dy not in star_dict[x + dx]:
            flg = False
            break
        else:
            selected.append([x + dx, y + dy])
    if flg:
        break

seiza.sort(key=lambda s: (s[0], s[1]))
selected.sort(key=lambda s: (s[0], s[1]))

dx = selected[0][0] - seiza[0][0]
dy = selected[0][1] - seiza[0][1]

print(dx, dy)