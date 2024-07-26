from collections import defaultdict, deque


N = int(input())
AB = [list(map(int, input().split())) for i in range(N - 1)]

G = defaultdict(list)
for a,b in AB:
    G[a].append(b)
    G[b].append(a)


queue = deque([[1, 1]])
green = []
red = []
visited = [False] * (N + 1)
while queue:
    node, color = queue.pop()
    if visited[node]:
        continue
    visited[node] = True
    if color == 0:
        green.append(node)
    else:
        red.append(node)
    for next in G[node]:
        cl = 1 - color
        queue.append([next, cl])
    
if len(green) > len(red):
    print(*green[:(N // 2)])
else:
    print(*red[:(N // 2)])