import heapq
N, M, X = map(int,input().split())
H = [int(input()) for _ in range(N)]
edges = [[] for _ in range(N)]
for _ in range(M):
  a, b, t = map(int,input().split())
  if H[a-1] >= t:edges[a-1].append([b-1,t])
  if H[b-1] >= t:edges[b-1].append([a-1,t])
dp = [float("inf")]*N
dp[0] = 0
hq = []
heapq.heappush(hq,[0,0])
while hq:
  _, v = heapq.heappop(hq)
  now_h = max(X-dp[v],0)
  for edge in edges[v]:
    nex_v, t = edge
    cost = 0
    if now_h - t > H[nex_v]: cost = now_h - H[nex_v]
    elif now_h - t < 0: cost = t*2 - now_h
    else: cost = t
    if dp[v] + cost < dp[nex_v]:
      dp[nex_v] = dp[v] + cost
      heapq.heappush(hq,[dp[v]+cost,nex_v])
if dp[-1] == float("inf"):
  print(-1)
else:
  print(dp[-1]+H[-1]-max(0,X-dp[-1]))