INF = 1 << 61

class Edge:
    def __init__(self, to, cap, rev) -> None:
        self.to = to
        self.cap = cap
        self.rev = rev
    
class FordFulkerson:
    def __init__(self, N) -> None:
        self.size = N
        self.g = [[] for _ in range(N)]
        self.visited = [False] * N
    
    def add_edge(self, a, b, c):
        g = self.g
        e = Edge(b, c, None)
        rev = Edge(a, 0, e)
        e.rev = rev
        g[a].append(e)
        g[b].append(rev)
    
    def dfs(self, i, goal, F):
        if i == goal:
            return F
        self.visited[i] = True
        
        for e in self.g[i]:
            if e.cap == 0:
                continue
            if self.visited[e.to]:
                continue
            flow = self.dfs(e.to, goal, min(F, e.cap))

            if flow:
                e.cap -= flow
                e.rev.cap += flow
                return flow
        
        return 0
    
    def max_flow(self, s, t):
        ans = 0
        while True:
            self.visited = [False] * self.size
            F = self.dfs(s, t, INF)
            if F == 0:
                break
            ans += F
        return ans
    


N, M = map(int, input().split())
C = [input() for _ in range(N)]

S = N + 24
T = S + 1
g = FordFulkerson(T + 1)

for i in range(N):
    c = C[i]
    g.add_edge(S, i, 10)
    for j, c in enumerate(c):
        if c == '1':
            g.add_edge(i, N + j, 1)

for j in range(24):
    g.add_edge(N + j, T, M)

print("Yes" if g.max_flow(S, T) == M * 24 else "No")