import heapq

N = int(input())
G = {}

for i in range(N):
    ukv = list(map(int, input().split()))
    if ukv[1] == 0:
        G[ukv[0]] = []
    else:
        G[ukv[0]] = ukv[2:]


INF = 10 ** 10
def bfs(start: int):
    cnt = [INF] * (N + 1)
    cnt[start] = 0
    queue = [start]
    while queue:
        c = heapq.heappop(queue)
        g = G[c]
        for gg in g:
            if cnt[gg] > cnt[c] + 1:
                cnt[gg] = cnt[c] + 1
                heapq.heappush(queue, gg)
    return cnt

ans = bfs(1)
for i in range(1, N + 1):
    if i > 1 and ans[i] == INF:
        print(i, -1)
    else:
        print(i, ans[i])