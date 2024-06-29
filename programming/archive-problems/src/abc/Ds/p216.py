from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
indeg = [0] * N
for _ in range(M):
  k = int(input())
  A = list(map(int, input().split()))
  for f, t in zip(A, A[1:]):
    f -= 1
    t -= 1
    G[f].append(t)
    indeg[t] += 1
    
q = deque()
for i in range(N):
  if indeg[i] == 0:
    q.append(i)
    
ans = []
while q:
  v = q.popleft()
  ans.append(v)
  for chi in G[v]:
    indeg[chi] -= 1
    if indeg[chi] == 0:
      q.append(chi)
      
if len(ans) == N:
  print('Yes')
else:
  print('No')