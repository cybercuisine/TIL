from collections import deque


def make_start():
    start = ["9"] * 9
    for piece, v in enumerate(P, 1):
        start[v] = str(piece)
    return start

def bfs(start):
    def to_str(state):  
        return ''.join(state)  

    goal = [str(i + 1) for i in range(9)]  
    seen = set() 
    que = deque()
    que.append((start, 0)) 

    while que:
        state, d = que.popleft()

        if state == goal:
            return d

        u_empty = state.index("9") 
        for v in G[u_empty]:
            n_state = state[:] 
            n_state[u_empty], n_state[v] = n_state[v], n_state[u_empty] 
            ns_str = to_str(n_state)  
            if ns_str not in seen:
                seen.add(ns_str)
                que.append((n_state, d + 1))
    return -1


M = int(input())
G = [[] for _ in range(9)]  
for _ in range(M):
    u, v = (x - 1 for x in map(int, input().split()))
    G[u].append(v)
    G[v].append(u)

P = [x - 1 for x in map(int, input().split())]  
start = make_start()  
print(bfs(start))


