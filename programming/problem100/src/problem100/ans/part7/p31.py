import queue

d_odd = ((-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1))
d_even = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1))

W, H = map(int, input().split())

mp = [[0] * (W + 2)]
for h in range(H):
    s = list(map(int, input().split()))
    mp.append([0] + s + [0])
mp.append([0] * (W + 2))
visited = [[0] * (W + 2) for _ in range(H + 2)]

ans = 0
q = queue.Queue()
q.put((0, 0))
while not q.empty():
    y, x = q.get()
    if visited[y][x] == 1:
        continue

    visited[y][x] = 1
    if y % 2 == 0:
        d = d_even
    else:
        d = d_odd
    for dx, dy in d:
        if (0 <= x + dx < W + 2) and (0 <= y + dy < H + 2):
            if mp[y + dy][x + dx] == 1:
                ans += 1
            else:
                if visited[y + dy][x + dx] == 0:
                    q.put((y + dy, x + dx))

print(ans)
